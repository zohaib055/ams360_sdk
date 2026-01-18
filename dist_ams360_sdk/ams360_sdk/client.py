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
            f"<a:EmployeeCode>{escape(employee_code)}</a:EmployeeCode>"
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
            f"<a:AgencyNo>{escape(agency_no)}</a:AgencyNo>"
            f"<a:LoginId>{escape(login_id)}</a:LoginId>"
            f"<a:Password>{escape(password)}</a:Password>"
            f"{employee_xml}"
            "</Request>"
            "</Login>"
            "</s:Body>"
            "</s:Envelope>"
        )

        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://www.WSAPI.AMS360.com/v3.0/WSAPIServiceContract/Login",
        }

        self.last_login_request = body
        masked_body = body.replace(
            f"<a:Password>{escape(password)}</a:Password>",
            "<a:Password>***</a:Password>",
        )
        self._debug("Login request (masked):\n" + masked_body)

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
        masked_response = re.sub(r"(<Ticket>)(.*?)(</Ticket>)", r"\1***\3", xml_text, flags=re.DOTALL)
        self._debug("Login response:\n" + masked_response)
        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as f:
            raise AMS360AuthError(f"Login response parse error: {f}") from f

        ticket = None
        for node in root.iter():
            if node.tag.endswith("Ticket") and node.text and node.text.strip():
                ticket = node.text.strip()
                break

        if not ticket:
            snippet = xml_text.strip()
            if len(snippet) > 2000:
                snippet = snippet[:2000] + "... (truncated)"
            raise AMS360AuthError(f"Login failed; Ticket not found. SOAP response: {snippet}")
        self.ticket = str(ticket)

        self.client.set_default_soapheaders({"WSAPISession": {"Ticket": self.ticket}})
        return self.ticket

    def last_login_soap(self) -> Dict[str, str]:
        return {
            "request": self.last_login_request or "",
            "response": self.last_login_response or "",
        }

    def call(self, op_name: str, **kwargs: Any) -> Any:
        fn = getattr(self.client.service, op_name, None)
        if not fn:
            raise AttributeError(f"Operation '{op_name}' not found in WSDL")
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
        return {"sent": sent, "received": recv}
