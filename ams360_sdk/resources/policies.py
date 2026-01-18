from __future__ import annotations
from typing import Any
from ..client import AMS360Client, NS_DC

class PoliciesResource:
    def __init__(self, ams: AMS360Client) -> None:
        self.ams = ams

    def get(self, policy_id: str) -> Any:
        factory = self.ams.soap.client.type_factory(NS_DC)
        req = factory.PolicyGetRequest(PolicyId=policy_id)
        return self.ams.call("PolicyGet", Request=req)
