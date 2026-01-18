from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from .config import AMS360Config
from .soap import SoapClient
from .errors import AMS360AuthError, AMS360OperationNotFound

# Resources
#from .resources.agency import AgencyResource
#from .resources.customers import CustomersResource
#from .resources.policies import PoliciesResource

NS_V3 = "http://www.WSAPI.AMS360.com/v3.0"
NS_DC = "http://www.WSAPI.AMS360.com/v3.0/DataContract"

@dataclass
class AuthState:
    ticket: Optional[str] = None

class AMS360Client:
    """
    REST-like facade:
    - ams.auth.login()
    - ams.agency.get_info()
    - ams.customers.get(...)
    - ams.policies.get(...)
    """
    def __init__(self, cfg: AMS360Config) -> None:
        self.cfg = cfg
        self.soap = SoapClient(cfg)
        self.auth = AuthState()

        from .resources.agency import AgencyResource
        from .resources.customers import CustomersResource
        from .resources.policies import PoliciesResource
        
        self.agency = AgencyResource(self)
        self.customers = CustomersResource(self)
        self.policies = PoliciesResource(self)

    @staticmethod
    def from_env() -> "AMS360Client":
        return AMS360Client(AMS360Config.from_env())

    # ---------- Authentication ----------
    def login(self) -> str:
        """
        Calls WSAPI v3 Login. Stores ticket and sets default SOAP header for subsequent calls.
        Works with empty EmployeeCode if your tenant maps 'Specific Employee = WSAPI' in Web Service API Setup.
        """
        if not self.cfg.agency_no or not self.cfg.login_id or not self.cfg.password:
            raise AMS360AuthError("Missing AMS360_AGENCY_NO / AMS360_LOGIN_ID / AMS360_PASSWORD")

        factory = self.soap.client.type_factory(NS_DC)

        # WSAPIRequest is in DataContract
        req = factory.WSAPIRequest(
            AgencyNo=self.cfg.agency_no,
            LoginId=self.cfg.login_id,
            Password=self.cfg.password,
            EmployeeCode=(self.cfg.employee_code or None),
        )

        result = self.soap.call("Login", Request=req)

        ticket = getattr(result, "Ticket", None) or getattr(result, "ticket", None)
        if not ticket:
            raise AMS360AuthError("Login succeeded but no Ticket returned")

        self.auth.ticket = str(ticket)

        # Apply default session header for all future calls
        # Zeep will serialize dict headers into SOAP headers.
        self.soap.client.set_default_soapheaders({
            "WSAPISession": {"Ticket": self.auth.ticket}
        })

        return self.auth.ticket

    def ensure_login(self) -> None:
        if not self.auth.ticket:
            self.login()

    # ---------- Generic call ----------
    def call(self, op_name: str, **kwargs: Any) -> Any:
        """
        Generic call that ensures auth and executes.
        """
        self.ensure_login()
        try:
            return self.soap.call(op_name, **kwargs)
        except AttributeError as e:
            raise AMS360OperationNotFound(str(e)) from e

    # ---------- Debug helpers ----------
    def last_soap(self) -> Dict[str, str]:
        return {
            "sent": self.soap.debug.last_sent,
            "received": self.soap.debug.last_received,
        }
