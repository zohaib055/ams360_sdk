import os
import re
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests
from zeep import Client, Settings
from zeep.transports import Transport
from zeep.helpers import serialize_object

DEFAULT_WSDL = os.getenv("AMS360_WSDL_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc?wsdl")
DEFAULT_ENDPOINT = os.getenv("AMS360_ENDPOINT_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc")

OUT_DIR = Path("ams360_generated")
PKG_DIR = OUT_DIR / "ams360_sdk"

def safe_py_name(name: str) -> str:
    # Convert SOAP OpName -> pythonic method name, avoid keywords
    s = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if re.match(r"^\d", s):
        s = f"op_{s}"
    if s in {"class", "def", "return", "from", "import", "pass", "global", "lambda"}:
        s = f"{s}_"
    return s

def load_client(wsdl_url: str, endpoint_url: str) -> Client:
    session = requests.Session()
    transport = Transport(session=session, timeout=60, operation_timeout=120)
    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(wsdl=wsdl_url, transport=transport, settings=settings)

    # Force endpoint address (some WSDLs embed a different host)
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            port.binding_options["address"] = endpoint_url

    return client

def list_operations(client: Client) -> List[Tuple[str, str, str]]:
    ops: List[Tuple[str, str, str]] = []
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            for op_name in port.binding._operations.keys():
                ops.append((service.name, port.name, op_name))
    # De-dupe while preserving order
    seen = set()
    out = []
    for x in ops:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

def op_signature(client: Client, service_name: str, port_name: str, op_name: str) -> Dict[str, Any]:
    service = client.wsdl.services[service_name]
    port = service.ports[port_name]
    op = port.binding._operations[op_name]

    # Zeep exposes the input message signature here:
    # op.input.signature() gives something like: "Request: ns0:WSAPIRequest"
    sig = str(op.input.signature())
    return {
        "service": service_name,
        "port": port_name,
        "operation": op_name,
        "input_signature": sig,
        "doc": (op.input.body.type.name if getattr(op.input, "body", None) else None),
    }

def write_files(client: Client) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PKG_DIR.mkdir(parents=True, exist_ok=True)

    ops = list_operations(client)
    catalog = [op_signature(client, s, p, o) for (s, p, o) in ops]

    # ---- Write catalog JSON (for quick browsing / building UIs) ----
    (OUT_DIR / "operations.json").write_text(json.dumps(catalog, indent=2), encoding="utf-8")

    # ---- __init__.py ----
    (PKG_DIR / "__init__.py").write_text(
        "from .client import AMS360Client\n"
        "from .generated import GeneratedEndpoints\n"
        "__all__ = ['AMS360Client', 'GeneratedEndpoints']\n",
        encoding="utf-8",
    )

    # ---- errors.py ----
    (PKG_DIR / "errors.py").write_text(
        "class AMS360Error(Exception):\n"
        "    pass\n\n"
        "class AMS360AuthError(AMS360Error):\n"
        "    pass\n\n"
        "class AMS360SoapError(AMS360Error):\n"
        "    pass\n",
        encoding="utf-8",
    )

    # ---- client.py (login + call + SOAP debug) ----
    (PKG_DIR / "client.py").write_text(
        '''import os
from typing import Any, Dict, Optional

import requests
from zeep import Client, Settings
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault
from zeep.helpers import serialize_object

from .errors import AMS360AuthError, AMS360SoapError

NS_DC = "http://www.WSAPI.AMS360.com/v3.0/DataContract"

class AMS360Client:
    def __init__(
        self,
        wsdl_url: str,
        endpoint_url: str,
        timeout: int = 60,
        operation_timeout: int = 120,
        verify_tls: bool = True,
    ) -> None:
        self.history = HistoryPlugin()
        session = requests.Session()
        session.verify = verify_tls

        transport = Transport(session=session, timeout=timeout, operation_timeout=operation_timeout)
        settings = Settings(strict=False, xml_huge_tree=True)

        self.client = Client(wsdl=wsdl_url, transport=transport, settings=settings, plugins=[self.history])

        # Force endpoint
        for service in self.client.wsdl.services.values():
            for port in service.ports.values():
                port.binding_options["address"] = endpoint_url

        self.ticket: Optional[str] = None

    @staticmethod
    def from_env() -> "AMS360Client":
        wsdl_url = os.getenv("AMS360_WSDL_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc?wsdl")
        endpoint_url = os.getenv("AMS360_ENDPOINT_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc")
        verify_tls = os.getenv("AMS360_VERIFY_TLS", "true").lower() != "false"
        return AMS360Client(wsdl_url=wsdl_url, endpoint_url=endpoint_url, verify_tls=verify_tls)

    def login(self, agency_no: str, login_id: str, password: str, employee_code: str = "") -> str:
        factory = self.client.type_factory(NS_DC)

        # WSAPIRequest is DataContract; employee_code can be "" if your tenant maps "Specific Employee = WSAPI"
        req = factory.WSAPIRequest(
            AgencyNo=agency_no,
            LoginId=login_id,
            Password=password,
            EmployeeCode=(employee_code or None),
        )

        try:
            result = self.client.service.Login(Request=req)
        except Fault as f:
            raise AMS360AuthError(str(f)) from f

        ticket = getattr(result, "Ticket", None) or getattr(result, "ticket", None)
        if not ticket:
            raise AMS360AuthError("Login succeeded but no Ticket returned")
        self.ticket = str(ticket)

        # Default header for all calls
        self.client.set_default_soapheaders({"WSAPISession": {"Ticket": self.ticket}})
        return self.ticket

    def call(self, op_name: str, **kwargs: Any) -> Any:
        fn = getattr(self.client.service, op_name, None)
        if not fn:
            raise AttributeError(f"Operation '{op_name}' not found on this WSDL")
        try:
            res = fn(**kwargs)
            return res
        except Fault as f:
            raise AMS360SoapError(str(f)) from f

    def call_json(self, op_name: str, **kwargs: Any) -> Dict[str, Any]:
        # Convenience: returns plain dict/list primitives
        res = self.call(op_name, **kwargs)
        return serialize_object(res)

    def last_soap(self) -> Dict[str, str]:
        sent = ""
        recv = ""
        if self.history.last_sent:
            sent = self.history.last_sent["envelope"].decode("utf-8")
        if self.history.last_received:
            recv = self.history.last_received["envelope"].decode("utf-8")
        return {"sent": sent, "received": recv}
''',
        encoding="utf-8",
    )

    # ---- generated.py (ALL endpoints, 1 method per op) ----
    lines = []
    lines.append("from typing import Any, Dict\n")
    lines.append("from zeep.helpers import serialize_object\n")
    lines.append("from .client import AMS360Client\n\n")
    lines.append("class GeneratedEndpoints:\n")
    lines.append("    def __init__(self, ams: AMS360Client) -> None:\n")
    lines.append("        self.ams = ams\n\n")
    lines.append("    def call(self, operation: str, **kwargs: Any) -> Any:\n")
    lines.append("        return self.ams.call(operation, **kwargs)\n\n")
    lines.append("    def call_json(self, operation: str, **kwargs: Any) -> Dict[str, Any]:\n")
    lines.append("        return self.ams.call_json(operation, **kwargs)\n\n")

    for (_, _, op_name) in ops:
        py = safe_py_name(op_name)
        lines.append(f"    def {py}(self, **kwargs: Any) -> Any:\n")
        lines.append(f"        \"\"\"SOAP operation: {op_name}\"\"\"\n")
        lines.append(f"        return self.ams.call('{op_name}', **kwargs)\n\n")

        lines.append(f"    def {py}_json(self, **kwargs: Any) -> Dict[str, Any]:\n")
        lines.append(f"        \"\"\"SOAP operation: {op_name} (serialized to dict)\"\"\"\n")
        lines.append(f"        return self.ams.call_json('{op_name}', **kwargs)\n\n")

    (PKG_DIR / "generated.py").write_text("".join(lines), encoding="utf-8")

    # ---- cli.py (list ops + call any op) ----
    (OUT_DIR / "cli.py").write_text(
        '''import os
import json
import argparse

from ams360_sdk.client import AMS360Client
from ams360_sdk.generated import GeneratedEndpoints

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--list-ops", action="store_true")
    p.add_argument("--login", action="store_true")
    p.add_argument("--call", type=str, default="")
    p.add_argument("--json", action="store_true")
    p.add_argument("--payload", type=str, default="{}")
    args = p.parse_args()

    ams = AMS360Client.from_env()
    gen = GeneratedEndpoints(ams)

    if args.list_ops:
        # load operations.json produced by generator
        with open("operations.json", "r", encoding="utf-8") as f:
            ops = json.load(f)
        for x in ops:
            print(f"{x['operation']}: {x['input_signature']}")
        return

    if args.login or args.call:
        agency_no = os.getenv("AMS360_AGENCY_NO", "")
        login_id = os.getenv("AMS360_LOGIN_ID", "")
        password = os.getenv("AMS360_PASSWORD", "")
        employee_code = os.getenv("AMS360_EMPLOYEE_CODE", "")
        ams.login(agency_no=agency_no, login_id=login_id, password=password, employee_code=employee_code)

    if args.call:
        payload = json.loads(args.payload)
        if args.json:
            print(json.dumps(gen.call_json(args.call, **payload), indent=2))
        else:
            print(gen.call(args.call, **payload))
        return

    p.print_help()

if __name__ == "__main__":
    main()
''',
        encoding="utf-8",
    )

def main() -> None:
    wsdl = os.getenv("AMS360_WSDL_URL", DEFAULT_WSDL)
    endpoint = os.getenv("AMS360_ENDPOINT_URL", DEFAULT_ENDPOINT)

    print(f"Loading WSDL: {wsdl}")
    client = load_client(wsdl, endpoint)
    write_files(client)

    print(f"✅ Generated SDK at: {OUT_DIR.resolve()}")
    print("Next:")
    print("  1) set env vars (AMS360_AGENCY_NO, AMS360_LOGIN_ID, AMS360_PASSWORD)")
    print("  2) python cli.py --list-ops")
    print("  3) python cli.py --login")
    print("  4) python cli.py --call AgencyInfoGet --json --payload '{}'")

if __name__ == "__main__":
    main()
