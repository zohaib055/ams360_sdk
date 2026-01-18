from dataclasses import dataclass
import os

@dataclass(frozen=True)
class AMS360Config:
    wsdl_url: str = "https://wsapi.ams360.com/v3/WSAPIService.svc?wsdl"
    endpoint_url: str = "https://wsapi.ams360.com/v3/WSAPIService.svc"
    agency_no: str = "8880006-1"
    login_id: str = "testuser"
    password: str = "wK1atfrjjY7"
    employee_code: str = ""  # can be empty if you mapped "Specific Employee = WSAPI" in AMS360
    timeout_seconds: int = 60
    operation_timeout_seconds: int = 120
    verify_tls: bool = True

    @staticmethod
    def from_env() -> "AMS360Config":
        return AMS360Config(
            wsdl_url=os.getenv("AMS360_WSDL_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc?wsdl"),
            endpoint_url=os.getenv("AMS360_ENDPOINT_URL", "https://wsapi.ams360.com/v3/WSAPIService.svc"),
            agency_no=os.getenv("AMS360_AGENCY_NO", "8880006-1"),
            login_id=os.getenv("AMS360_LOGIN_ID", "testuser"),
            password=os.getenv("AMS360_PASSWORD", "wK1atfrjjY7"),
            employee_code=os.getenv("AMS360_EMPLOYEE_CODE", ""),  # optional for your setup
            timeout_seconds=int(os.getenv("AMS360_TIMEOUT", "60")),
            operation_timeout_seconds=int(os.getenv("AMS360_OPERATION_TIMEOUT", "120")),
            verify_tls=os.getenv("AMS360_VERIFY_TLS", "true").lower() != "false",
        )
