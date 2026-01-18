from __future__ import annotations
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import AMS360Client  # type-only import (prevents circular import)

class AgencyResource:
    def __init__(self, ams: "AMS360Client") -> None:
        self.ams = ams

    def get_info(self) -> Dict[str, Any]:
        res = self.ams.call("AgencyInfoGet")
        # return zeep objects as-is; you can serialize later if you want
        return {"raw": res}
