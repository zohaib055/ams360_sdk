import json
import os
import sys
from xml.etree import ElementTree as ET
from pathlib import Path

SDK_DIR = Path(__file__).resolve().parent / "dist_ams360_sdk"
sys.path.insert(0, str(SDK_DIR))

from ams360_sdk import AMS360Client, Generated, models
from ams360_sdk.errors import AMS360AuthError


def main() -> None:
    # TODO: Replace these with your AMS360 credentials or keep login.xml up to date.
    agency_no = ""
    login_id = ""
    password = ""
    employee_code = ""

    wsdl_path = SDK_DIR / "merged.wsdl"
    if not wsdl_path.exists():
        print(f"Missing WSDL: {wsdl_path}")
        sys.exit(1)

    login_xml_path = Path(__file__).resolve().parent / "login.xml"
    if login_xml_path.exists():
        xml_root = ET.parse(login_xml_path).getroot()
        for node in xml_root.iter():
            if node.tag.endswith("AgencyNo") and node.text:
                agency_no = node.text.strip()
            elif node.tag.endswith("LoginId") and node.text:
                login_id = node.text.strip()
            elif node.tag.endswith("Password") and node.text:
                password = node.text.strip()
            elif node.tag.endswith("EmployeeCode") and node.text:
                employee_code = node.text.strip()

    if not agency_no or not login_id or not password:
        print("Missing credentials. Update login.xml or set the values in example_app.py.")
        sys.exit(1)

    ams = AMS360Client(wsdl_path=str(wsdl_path), debug=True)
    try:
        ticket = ams.login(
            agency_no=agency_no,
            login_id=login_id,
            password=password,
            employee_code=employee_code,
        )
    except AMS360AuthError as exc:
        soap = ams.last_login_soap()
        req_path = Path(__file__).resolve().parent / "login_request.xml"
        resp_path = Path(__file__).resolve().parent / "login_response.xml"
        req_path.write_text(soap.get("request", ""), encoding="utf-8")
        resp_path.write_text(soap.get("response", ""), encoding="utf-8")
        print(f"Login failed: {exc}")
        print(f"Wrote request/response to {req_path} and {resp_path}")
        raise

    token_path = Path(__file__).resolve().parent / "ams360_ticket.txt"
    token_path.write_text(ticket, encoding="utf-8")

    gen = Generated(ams)

    def extract_customer_list(payload: object) -> list[dict]:
        if not payload:
            return []
        if isinstance(payload, dict):
            result = payload.get("CustomerGetListByNamePrefixResult", payload)
            if isinstance(result, dict):
                info_list = result.get("CustomerInfoList") or result.get("CustomerInfo")
                if isinstance(info_list, dict):
                    info_list = info_list.get("CustomerInfo")
                if info_list is None:
                    return []
                if isinstance(info_list, list):
                    return [item for item in info_list if isinstance(item, dict)]
                if isinstance(info_list, dict):
                    return [info_list]
        return []

    prefixes_env = os.getenv("AMS360_CUSTOMER_PREFIXES", "")
    if prefixes_env:
        prefixes = [p.strip() for p in prefixes_env.split(",") if p.strip()]
    else:
        prefixes = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    customers: list[dict] = []
    seen: set[str] = set()
    for prefix in prefixes:
        request = models.CustomerGetListByNamePrefixRequest(NamePrefix=prefix)
        result = gen.customer_get_list_by_name_prefix_json(request=request)
        for customer in extract_customer_list(result):
            key = str(
                customer.get("CustomerId")
                or customer.get("CustomerNumber")
                or customer.get("FirmName")
                or customer.get("FirstName")
                or customer.get("LastName")
                or customer
            )
            if key in seen:
                continue
            seen.add(key)
            customers.append(customer)

    out_path = Path(__file__).resolve().parent / "customers.json"
    out_path.write_text(json.dumps(customers, indent=2), encoding="utf-8")
    print(f"Fetched {len(customers)} customers. Saved to {out_path}")


if __name__ == "__main__":
    main()
