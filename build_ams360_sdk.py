import argparse
import json
import os
import re
import sys
import zipfile
from pathlib import Path

import requests
from lxml import etree
from zeep import Client, Settings
from zeep.transports import Transport


WSDL_NS = {"wsdl": "http://schemas.xmlsoap.org/wsdl/"}
XSD_NS = "http://www.w3.org/2001/XMLSchema"
SER_NS = "http://schemas.microsoft.com/2003/10/Serialization/"
PY_KEYWORDS = {
    "class",
    "def",
    "return",
    "from",
    "import",
    "pass",
    "global",
    "lambda",
}
XSD_TYPE_MAP = {
    "anyType": "Any",
    "base64Binary": "bytes",
    "boolean": "bool",
    "byte": "int",
    "date": "date",
    "dateTime": "datetime",
    "decimal": "Decimal",
    "double": "float",
    "float": "float",
    "int": "int",
    "integer": "int",
    "long": "int",
    "short": "int",
    "string": "str",
    "time": "time",
    "unsignedByte": "int",
    "unsignedInt": "int",
    "unsignedLong": "int",
    "unsignedShort": "int",
}


# ---------------------------
# WSDL merge + introspection
# ---------------------------

def merge_wsdl(service_wsdl: Path, contract_wsdl: Path, out_wsdl: Path) -> Path:
    """
    Merges binding(s) from WSAPIService.wsdl into WSAPIServiceContract.wsdl, producing merged.wsdl.
    This fixes the "0 operations" issue when one WSDL has bindings and the other has services/portType.
    """
    svc_doc = etree.parse(str(service_wsdl))
    ctr_doc = etree.parse(str(contract_wsdl))

    svc_bindings = svc_doc.xpath("/wsdl:definitions/wsdl:binding", namespaces=WSDL_NS)
    if not svc_bindings:
        raise RuntimeError(f"No wsdl:binding found in {service_wsdl}")

    ctr_bindings = ctr_doc.xpath("/wsdl:definitions/wsdl:binding", namespaces=WSDL_NS)
    ctr_defs = ctr_doc.getroot()

    if ctr_bindings:
        print("Contract WSDL already has bindings; skipping merge of bindings.")
    else:
        for b in svc_bindings:
            ctr_defs.append(b)

    out_wsdl.write_bytes(etree.tostring(ctr_doc, pretty_print=True, xml_declaration=True, encoding="utf-8"))
    return out_wsdl


def zeep_client_from_local_wsdl(wsdl_path: Path) -> Client:
    session = requests.Session()
    transport = Transport(session=session, timeout=60, operation_timeout=120)
    settings = Settings(strict=False, xml_huge_tree=True)

    # IMPORTANT: On Windows, do NOT use file:// URLs; use absolute path.
    wsdl_abs = str(wsdl_path.resolve())
    return Client(wsdl=wsdl_abs, transport=transport, settings=settings)


def list_operations(client: Client):
    ops = []
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            for op_name in port.binding._operations.keys():
                ops.append(op_name)
    return sorted(set(ops))


def extract_soap_actions(wsdl_path: Path):
    doc = etree.parse(str(wsdl_path))
    ns = {
        "wsdl": "http://schemas.xmlsoap.org/wsdl/",
        "soap": "http://schemas.xmlsoap.org/wsdl/soap/",
    }
    mapping = {}
    for op in doc.xpath("//wsdl:binding/wsdl:operation", namespaces=ns):
        name = op.get("name")
        soap_op = op.find("soap:operation", namespaces=ns)
        action = soap_op.get("soapAction") if soap_op is not None else None
        if name:
            mapping[name] = action
    return mapping


# ---------------------------
# SDK generation
# ---------------------------

def safe_py_name(name: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if re.match(r"^\d", s):
        s = "op_" + s
    return s


def to_snake(name: str) -> str:
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    s = s2.replace("__", "_").lower()
    if re.match(r"^\d", s):
        s = "op_" + s
    if s in {"class", "def", "return", "from", "import", "pass", "global", "lambda"}:
        s += "_"
    return s


def safe_class_name(name: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if re.match(r"^\d", s):
        s = "Type_" + s
    if s in PY_KEYWORDS:
        s += "_"
    return s


def safe_field_name(name: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if re.match(r"^\d", s):
        s = "field_" + s
    if s in PY_KEYWORDS:
        s += "_"
    return s


def unique_name(name: str, used: set[str]) -> str:
    if name not in used:
        used.add(name)
        return name
    i = 1
    candidate = f"{name}_{i}"
    while candidate in used:
        i += 1
        candidate = f"{name}_{i}"
    used.add(candidate)
    return candidate


def _is_unbounded(max_occurs: object) -> bool:
    if max_occurs is None:
        return True
    if isinstance(max_occurs, str):
        return max_occurs == "unbounded"
    return False


def _is_multiple(max_occurs: object) -> bool:
    if _is_unbounded(max_occurs):
        return True
    if isinstance(max_occurs, str):
        return max_occurs.isdigit() and int(max_occurs) > 1
    return isinstance(max_occurs, int) and max_occurs > 1


def array_item_type(type_obj) -> str | None:
    elems = getattr(type_obj, "elements", None)
    if not elems or len(elems) != 1:
        return None
    _, elem = elems[0]
    if _is_multiple(elem.max_occurs):
        return python_type_for_type(elem.type)
    return None


def python_type_for_type(type_obj) -> str:
    qname = getattr(type_obj, "qname", None)
    if qname is not None:
        if qname.namespace == XSD_NS:
            return XSD_TYPE_MAP.get(qname.localname, "Any")
        if qname.namespace == SER_NS and qname.localname == "guid":
            return "str"

    if not hasattr(type_obj, "elements"):
        return "str"

    elems = getattr(type_obj, "elements", None)
    if elems is None or len(elems) == 0:
        return "str"

    return "Dict[str, Any]"


def python_type_for_element(element) -> str:
    if _is_multiple(element.max_occurs):
        return f"List[{python_type_for_type(element.type)}]"

    array_item = array_item_type(element.type)
    if array_item:
        return f"List[{array_item}]"

    return python_type_for_type(element.type)


def build_request_model_fields(req_type) -> list[dict[str, str]]:
    fields: list[dict[str, str]] = []
    used_names: set[str] = set()
    for xml_name, elem in list(getattr(req_type, "elements", [])):
        py_name = unique_name(safe_field_name(xml_name), used_names)
        py_type = python_type_for_element(elem)
        fields.append({"xml_name": xml_name, "py_name": py_name, "py_type": py_type})
    return fields


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def collect_request_models(client: Client) -> tuple[dict[str, list[dict[str, str]]], dict[str, str]]:
    request_models: dict[str, list[dict[str, str]]] = {}
    op_request_types: dict[str, str] = {}

    for service in client.wsdl.services.values():
        for port in service.ports.values():
            for op_name, op in port.binding._operations.items():
                body = op.input.body
                if not body or not getattr(body, "type", None):
                    continue

                elements = list(getattr(body.type, "elements", []))
                if not elements:
                    continue

                for elem_name, elem in elements:
                    if elem_name != "Request":
                        continue

                    req_type = elem.type
                    req_qname = getattr(req_type, "qname", None)
                    req_name = req_qname.localname if req_qname else req_type.__class__.__name__
                    class_name = safe_class_name(req_name)

                    op_request_types[op_name] = class_name
                    if class_name not in request_models:
                        request_models[class_name] = build_request_model_fields(req_type)
                    break

    return request_models, op_request_types


def generate_sdk(
    out_dir: Path,
    merged_wsdl: Path,
    operations: list[str],
    soap_actions: dict[str, str | None],
    request_models: dict[str, list[dict[str, str]]],
    op_request_types: dict[str, str],
):
    pkg_dir = out_dir / "ams360_sdk"
    pkg_dir.mkdir(parents=True, exist_ok=True)

    write_text(pkg_dir / "__init__.py",
               "from .client import AMS360Client\n"
               "from .generated import Generated\n"
               "from . import models\n"
               "__all__ = ['AMS360Client', 'Generated', 'models']\n")

    write_text(pkg_dir / "errors.py", """\
class AMS360Error(Exception):
    pass

class AMS360AuthError(AMS360Error):
    pass

class AMS360SoapError(AMS360Error):
    pass
""")

    model_lines = []
    model_lines.append("from dataclasses import asdict, dataclass, fields, is_dataclass\n")
    model_lines.append("from datetime import date, datetime, time\n")
    model_lines.append("from decimal import Decimal\n")
    model_lines.append("from typing import Any, ClassVar, Dict, List, Optional\n\n")
    model_lines.append("def _serialize_value(value: Any) -> Any:\n")
    model_lines.append("    if isinstance(value, RequestModel):\n")
    model_lines.append("        return value.to_dict()\n")
    model_lines.append("    if is_dataclass(value):\n")
    model_lines.append("        return asdict(value)\n")
    model_lines.append("    if isinstance(value, list):\n")
    model_lines.append("        return [_serialize_value(item) for item in value]\n")
    model_lines.append("    if isinstance(value, dict):\n")
    model_lines.append("        return {k: _serialize_value(v) for k, v in value.items()}\n")
    model_lines.append("    return value\n\n")
    model_lines.append("@dataclass\n")
    model_lines.append("class RequestModel:\n")
    model_lines.append("    __field_map__: ClassVar[Dict[str, str]] = {}\n\n")
    model_lines.append("    def to_dict(self) -> Dict[str, Any]:\n")
    model_lines.append("        data: Dict[str, Any] = {}\n")
    model_lines.append("        for f in fields(self):\n")
    model_lines.append("            value = getattr(self, f.name)\n")
    model_lines.append("            if value is None:\n")
    model_lines.append("                continue\n")
    model_lines.append("            key = self.__field_map__.get(f.name, f.name)\n")
    model_lines.append("            data[key] = _serialize_value(value)\n")
    model_lines.append("        return data\n\n")

    for model_name in sorted(request_models):
        fields = request_models[model_name]
        model_lines.append("@dataclass\n")
        model_lines.append(f"class {model_name}(RequestModel):\n")
        if fields:
            for field in fields:
                type_str = f"Optional[{field['py_type']}]"
                model_lines.append(f"    {field['py_name']}: {type_str} = None\n")
        field_map = {f["py_name"]: f["xml_name"] for f in fields if f["py_name"] != f["xml_name"]}
        model_lines.append(f"    __field_map__: ClassVar[Dict[str, str]] = {repr(field_map)}\n\n")

    write_text(pkg_dir / "models.py", "".join(model_lines))

    write_text(pkg_dir / "client.py", f"""\
import os
import re
from typing import Any, Dict, Optional
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

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
        wsdl_path: str,
        endpoint_url: str = "https://wsapi.ams360.com/v3/WSAPIService.svc",
        timeout: int = 60,
        operation_timeout: int = 120,
        verify_tls: bool = True,
        debug: bool = False,
    ) -> None:
        self.history = HistoryPlugin()
        session = requests.Session()
        session.verify = verify_tls

        self.session = session
        self.endpoint_url = endpoint_url
        self.timeout = timeout
        self.debug = debug
        self.last_login_request: Optional[str] = None
        self.last_login_response: Optional[str] = None

        transport = Transport(session=session, timeout=timeout, operation_timeout=operation_timeout)
        settings = Settings(strict=False, xml_huge_tree=True)

        self.client = Client(wsdl=wsdl_path, transport=transport, settings=settings, plugins=[self.history])

        for service in self.client.wsdl.services.values():
            for port in service.ports.values():
                port.binding_options["address"] = endpoint_url

        self.ticket: Optional[str] = None

    @staticmethod
    def from_env(wsdl_path: str) -> "AMS360Client":
        endpoint = os.getenv("AMS360_ENDPOINT_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc")
        verify_tls = os.getenv("AMS360_VERIFY_TLS", "true").lower() != "false"
        return AMS360Client(wsdl_path=wsdl_path, endpoint_url=endpoint, verify_tls=verify_tls)

    def _debug(self, message: str) -> None:
        if self.debug:
            print(message)

    def login(self, agency_no: str, login_id: str, password: str, employee_code: str = "") -> str:
        agency_no = agency_no or ""
        login_id = login_id or ""
        password = password or ""
        employee_code = employee_code or ""

        employee_xml = (
            f"<a:EmployeeCode>{{escape(employee_code)}}</a:EmployeeCode>"
            if employee_code
            else "<a:EmployeeCode/>"
        )

        body = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">'
            "<s:Body>"
            '<Login xmlns="http://www.WSAPI.AMS360.com/v3.0">'
            '<Request xmlns:a="http://www.WSAPI.AMS360.com/v3.0/DataContract" '
            'xmlns:i="http://www.w3.org/2001/XMLSchema-instance">'
            f"<a:AgencyNo>{{escape(agency_no)}}</a:AgencyNo>"
            f"<a:LoginId>{{escape(login_id)}}</a:LoginId>"
            f"<a:Password>{{escape(password)}}</a:Password>"
            f"{{employee_xml}}"
            "</Request>"
            "</Login>"
            "</s:Body>"
            "</s:Envelope>"
        )

        headers = {{
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://www.WSAPI.AMS360.com/v3.0/WSAPIServiceContract/Login",
        }}

        self.last_login_request = body
        masked_body = body.replace(
            f"<a:Password>{{escape(password)}}</a:Password>",
            "<a:Password>***</a:Password>",
        )
        self._debug("Login request (masked):\\n" + masked_body)

        try:
            resp = self.session.post(
                self.endpoint_url,
                data=body.encode("utf-8"),
                headers=headers,
                timeout=self.timeout,
            )
        except requests.RequestException as f:
            raise AMS360AuthError(str(f)) from f

        xml_text = resp.text or ""
        self.last_login_response = xml_text
        masked_response = re.sub(r"(<Ticket>)(.*?)(</Ticket>)", r"\\1***\\3", xml_text, flags=re.DOTALL)
        self._debug("Login response:\\n" + masked_response)
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as f:
            raise AMS360AuthError(f"Login response parse error: {{f}}") from f

        ticket = None
        for node in root.iter():
            if node.tag.endswith("Ticket") and node.text and node.text.strip():
                ticket = node.text.strip()
                break

        if not ticket:
            snippet = xml_text.strip()
            if len(snippet) > 2000:
                snippet = snippet[:2000] + "... (truncated)"
            raise AMS360AuthError(f"Login failed; Ticket not found. SOAP response: {{snippet}}")
        self.ticket = str(ticket)

        self.client.set_default_soapheaders({{"WSAPISession": {{"Ticket": self.ticket}}}})
        return self.ticket

    def last_login_soap(self) -> Dict[str, str]:
        return {{
            "request": self.last_login_request or "",
            "response": self.last_login_response or "",
        }}

    def call(self, op_name: str, **kwargs: Any) -> Any:
        fn = getattr(self.client.service, op_name, None)
        if not fn:
            raise AttributeError(f"Operation '{{op_name}}' not found in WSDL")
        try:
            return fn(**kwargs)
        except Fault as f:
            raise AMS360SoapError(str(f)) from f

    def call_json(self, op_name: str, **kwargs: Any) -> Dict[str, Any]:
        return serialize_object(self.call(op_name, **kwargs))

    def last_soap(self) -> Dict[str, str]:
        sent = ""
        recv = ""
        if self.history.last_sent:
            sent = self.history.last_sent["envelope"].decode("utf-8")
        if self.history.last_received:
            recv = self.history.last_received["envelope"].decode("utf-8")
        return {{"sent": sent, "received": recv}}
""")

    gen_lines = []
    gen_lines.append("from dataclasses import asdict, is_dataclass\n")
    gen_lines.append("from typing import Any, Dict, Optional, Union\n")
    if request_models:
        gen_lines.append("from .models import (\n")
        for model_name in sorted(request_models):
            gen_lines.append(f"    {model_name},\n")
        gen_lines.append(")\n")
    gen_lines.append("from .client import AMS360Client\n\n")
    gen_lines.append("class Generated:\n")
    gen_lines.append("    def __init__(self, ams: AMS360Client) -> None:\n")
    gen_lines.append("        self.ams = ams\n\n")
    gen_lines.append("    @staticmethod\n")
    gen_lines.append("    def _normalize_request(request: Any) -> Any:\n")
    gen_lines.append("        if request is None:\n")
    gen_lines.append("            return None\n")
    gen_lines.append("        if hasattr(request, \"to_dict\"):\n")
    gen_lines.append("            return request.to_dict()\n")
    gen_lines.append("        if is_dataclass(request):\n")
    gen_lines.append("            return asdict(request)\n")
    gen_lines.append("        return request\n\n")
    gen_lines.append("    def call(self, operation: str, **kwargs: Any) -> Any:\n")
    gen_lines.append("        return self.ams.call(operation, **kwargs)\n\n")
    gen_lines.append("    def call_json(self, operation: str, **kwargs: Any) -> Dict[str, Any]:\n")
    gen_lines.append("        return self.ams.call_json(operation, **kwargs)\n\n")

    for op in operations:
        pas = safe_py_name(op)
        sn = to_snake(op)
        req_type = op_request_types.get(op)

        if req_type:
            req_sig = f"Optional[Union[{req_type}, Dict[str, Any]]]"
            gen_lines.append(f"    def {sn}(self, request: {req_sig} = None, **kwargs: Any) -> Any:\n")
            gen_lines.append(f"        \"\"\"{op}\"\"\"\n")
            gen_lines.append("        if request is not None:\n")
            gen_lines.append("            kwargs[\"Request\"] = self._normalize_request(request)\n")
            gen_lines.append(f"        return self.ams.call('{op}', **kwargs)\n\n")

            gen_lines.append(f"    def {sn}_json(self, request: {req_sig} = None, **kwargs: Any) -> Dict[str, Any]:\n")
            gen_lines.append(f"        \"\"\"{op} (JSON)\"\"\"\n")
            gen_lines.append("        if request is not None:\n")
            gen_lines.append("            kwargs[\"Request\"] = self._normalize_request(request)\n")
            gen_lines.append(f"        return self.ams.call_json('{op}', **kwargs)\n\n")

            if pas != sn:
                gen_lines.append(f"    def {pas}(self, request: {req_sig} = None, **kwargs: Any) -> Any:\n")
                gen_lines.append(f"        \"\"\"{op} (original op name wrapper)\"\"\"\n")
                gen_lines.append("        if request is not None:\n")
                gen_lines.append("            kwargs[\"Request\"] = self._normalize_request(request)\n")
                gen_lines.append(f"        return self.ams.call('{op}', **kwargs)\n\n")
        else:
            gen_lines.append(f"    def {sn}(self, **kwargs: Any) -> Any:\n")
            gen_lines.append(f"        \"\"\"{op}\"\"\"\n")
            gen_lines.append(f"        return self.ams.call('{op}', **kwargs)\n\n")

            gen_lines.append(f"    def {sn}_json(self, **kwargs: Any) -> Dict[str, Any]:\n")
            gen_lines.append(f"        \"\"\"{op} (JSON)\"\"\"\n")
            gen_lines.append(f"        return self.ams.call_json('{op}', **kwargs)\n\n")

            if pas != sn:
                gen_lines.append(f"    def {pas}(self, **kwargs: Any) -> Any:\n")
                gen_lines.append(f"        \"\"\"{op} (original op name wrapper)\"\"\"\n")
                gen_lines.append(f"        return self.ams.call('{op}', **kwargs)\n\n")

    write_text(pkg_dir / "generated.py", "".join(gen_lines))

    write_text(pkg_dir / "cli.py", f"""\
import argparse
import json
import os
import sys

from .client import AMS360Client
from .generated import Generated

def main():
    p = argparse.ArgumentParser(prog="ams360_sdk.cli")
    p.add_argument("--wsdl", default="{merged_wsdl.name}", help="Local merged WSDL filename")
    p.add_argument("--list-ops", action="store_true", help="List operations")
    p.add_argument("--login", action="store_true", help="Login and print ticket")
    p.add_argument("--call", type=str, default="", help="Call operation by name")
    p.add_argument("--payload", type=str, default="{{}}", help="JSON payload dict for kwargs")
    p.add_argument("--json", action="store_true", help="Serialize response to JSON")
    args = p.parse_args()

    wsdl_path = os.path.abspath(args.wsdl)
    if not os.path.exists(wsdl_path):
        print("❌ WSDL not found:", wsdl_path)
        sys.exit(1)

    ams = AMS360Client.from_env(wsdl_path=wsdl_path)
    gen = Generated(ams)

    if args.list_ops:
        ops_file = os.path.join(os.path.dirname(wsdl_path), "operations.json")
        if os.path.exists(ops_file):
            data = json.loads(open(ops_file, "r", encoding="utf-8").read())
            ops = [x["operation"] for x in data]
        else:
            ops = []
            for service in ams.client.wsdl.services.values():
                for port in service.ports.values():
                    for op in port.binding._operations.keys():
                        ops.append(op)
            ops = sorted(set(ops))

        print(f"Found {{len(ops)}} operations:")
        for op in ops:
            print(op)
        return

    if args.login or args.call:
        agency_no = os.getenv("AMS360_AGENCY_NO", "")
        login_id = os.getenv("AMS360_LOGIN_ID", "")
        password = os.getenv("AMS360_PASSWORD", "")
        employee_code = os.getenv("AMS360_EMPLOYEE_CODE", "")
        if not agency_no or not login_id or not password:
            print("❌ Missing env vars: AMS360_AGENCY_NO, AMS360_LOGIN_ID, AMS360_PASSWORD")
            sys.exit(1)

        ticket = ams.login(agency_no=agency_no, login_id=login_id, password=password, employee_code=employee_code)
        print("Ticket:", ticket)

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
""")

    ops_json = [{"operation": op, "soapAction": soap_actions.get(op)} for op in operations]
    write_text(out_dir / "operations.json", json.dumps(ops_json, indent=2))

    write_text(out_dir / "README.md", f"""\
# AMS360 WSAPI v3 Offline SDK (Generated)

This SDK was generated from your local WSDL files.

## Files
- `{merged_wsdl.name}`: merged WSDL used by Zeep (offline)
- `operations.json`: operation -> soapAction map
- `ams360_sdk/`: python package
  - `client.py`: login + call + call_json
  - `generated.py`: one method per operation
  - `cli.py`: list operations, login, call any operation

## Install deps
```bash
pip install zeep requests lxml
```

## Environment variables
```bash
AMS360_AGENCY_NO=8880006-1
AMS360_LOGIN_ID=testuser
AMS360_PASSWORD=...
AMS360_EMPLOYEE_CODE=   # optional if "Specific Employee = WSAPI" mapping is set
AMS360_ENDPOINT_URL=https://wsapi.ams360.com/v3/WSAPIService.svc
```

## Run CLI (list operations)
From the output folder:
```bash
python -m ams360_sdk.cli --list-ops
```

## Login + call AgencyInfoGet
```bash
python -m ams360_sdk.cli --login --call AgencyInfoGet --json --payload "{{}}"
```
""")

    return out_dir


def zip_dir(src_dir: Path, zip_path: Path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in src_dir.rglob("*"):
            if p.is_file():
                z.write(p, arcname=str(p.relative_to(src_dir)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--service-wsdl", default="WSAPIService.wsdl")
    p.add_argument("--contract-wsdl", default="WSAPIServiceContract.wsdl")
    p.add_argument("--out", default="dist_ams360_sdk", help="Output folder")
    p.add_argument("--zip", action="store_true", help="Also create dist_ams360_sdk.zip")
    args = p.parse_args()

    service_wsdl = Path(args.service_wsdl)
    contract_wsdl = Path(args.contract_wsdl)
    out_dir = Path(args.out)

    if not service_wsdl.exists():
        raise SystemExit(f"Missing file: {service_wsdl}")
    if not contract_wsdl.exists():
        raise SystemExit(f"Missing file: {contract_wsdl}")

    out_dir.mkdir(parents=True, exist_ok=True)
    merged_wsdl = out_dir / "merged.wsdl"

    merged = merge_wsdl(service_wsdl, contract_wsdl, merged_wsdl)
    print(f"OK: Merged WSDL written to: {merged}")

    client = zeep_client_from_local_wsdl(merged)
    ops = list_operations(client)
    print(f"OK: Zeep loaded operations: {len(ops)}")

    if len(ops) == 0:
        print("❌ Still 0 ops. The WSDL likely lacks a service/port bound to a binding after merge.")
        sys.exit(1)

    actions = extract_soap_actions(merged)
    request_models, op_request_types = collect_request_models(client)
    generate_sdk(
        out_dir=out_dir,
        merged_wsdl=merged,
        operations=ops,
        soap_actions=actions,
        request_models=request_models,
        op_request_types=op_request_types,
    )
    print(f"OK: SDK generated in: {out_dir.resolve()}")

    if args.zip:
        zip_path = Path(str(out_dir) + ".zip")
        zip_dir(out_dir, zip_path)
        print(f"OK: ZIP created: {zip_path.resolve()}")

    print("\\nNext commands:")
    print(f"  cd {out_dir}")
    print("  python -m ams360_sdk.cli --list-ops")
    print('  python -m ams360_sdk.cli --login --call AgencyInfoGet --json --payload "{}"')


if __name__ == "__main__":
    main()
