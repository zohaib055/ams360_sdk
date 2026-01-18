from __future__ import annotations
from typing import Any, Dict, Optional
from ..client import AMS360Client, NS_DC

class CustomersResource:
    def __init__(self, ams: AMS360Client) -> None:
        self.ams = ams

    def get(self, customer_number: str) -> Any:
        """
        Example: CustomerGet typically expects a Request object.
        Exact shape depends on WSDL types; we build via type_factory.
        """
        factory = self.ams.soap.client.type_factory(NS_DC)
        req = factory.CustomerGetRequest(CustomerNumber=customer_number)
        return self.ams.call("CustomerGet", Request=req)

    def search(self, name: str, max_results: int = 25) -> Any:
        """
        Placeholder example. Your WSDL likely has CustomerGetList / CustomerSearch.
        We'll wire it once you confirm the exact operation names present in your WSDL.
        """
        return {"todo": "list ops and bind CustomerSearch/CustomerGetList", "name": name, "max_results": max_results}
