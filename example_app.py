import json
import os
import sys
from pathlib import Path

SDK_DIR = Path(__file__).resolve().parent / "dist_ams360_sdk"
sys.path.insert(0, str(SDK_DIR))

from ams360_sdk import AMS360Client, AMS360Settings, Generated, models
from ams360_sdk.errors import AMS360AuthError


def main() -> None:
    settings = AMS360Settings.from_env()
    if not settings.ticket and not settings.has_credentials():
        print(
            "Missing credentials. Set AMS360_AGENCY_NO, AMS360_LOGIN_ID, "
            "AMS360_PASSWORD or AMS360_TICKET."
        )
        sys.exit(1)

    try:
        ams = AMS360Client.from_settings(
            settings=settings,
            debug=True,
            auto_login=True,
        )
        ams.ensure_ticket()
    except FileNotFoundError as exc:
        print(f"WSDL not found: {exc}")
        sys.exit(1)
    except AMS360AuthError as exc:
        print(f"Login failed: {exc}")
        raise

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
