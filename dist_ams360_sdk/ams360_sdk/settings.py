from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    try:
        return int(raw)
    except ValueError:
        return default


@dataclass
class AMS360Settings:
    agency_no: str
    login_id: str
    password: str
    employee_code: str = ""
    endpoint_url: str = "https://wsapi.ams360.com/v3/WSAPIService.svc"
    verify_tls: bool = True
    timeout: int = 60
    operation_timeout: int = 120
    ticket: Optional[str] = None

    @classmethod
    def from_env(cls) -> "AMS360Settings":
        return cls(
            agency_no=os.getenv("AMS360_AGENCY_NO", ""),
            login_id=os.getenv("AMS360_LOGIN_ID", ""),
            password=os.getenv("AMS360_PASSWORD", ""),
            employee_code=os.getenv("AMS360_EMPLOYEE_CODE", ""),
            endpoint_url=os.getenv(
                "AMS360_ENDPOINT_URL",
                "https://wsapi.ams360.com/v3/WSAPIService.svc",
            ),
            verify_tls=os.getenv("AMS360_VERIFY_TLS", "true").lower() != "false",
            timeout=_env_int("AMS360_TIMEOUT", 60),
            operation_timeout=_env_int("AMS360_OPERATION_TIMEOUT", 120),
            ticket=(os.getenv("AMS360_TICKET", "") or None),
        )

    def has_credentials(self) -> bool:
        return bool(self.agency_no and self.login_id and self.password)
