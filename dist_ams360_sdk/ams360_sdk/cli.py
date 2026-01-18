import argparse
import json
import os
import sys

from .client import AMS360Client
from .generated import Generated

def main():
    p = argparse.ArgumentParser(prog="ams360_sdk.cli")
    p.add_argument("--wsdl", default="merged.wsdl", help="Local merged WSDL filename")
    p.add_argument("--list-ops", action="store_true", help="List operations")
    p.add_argument("--login", action="store_true", help="Login and print ticket")
    p.add_argument("--call", type=str, default="", help="Call operation by name")
    p.add_argument("--payload", type=str, default="{}", help="JSON payload dict for kwargs")
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

        print(f"Found {len(ops)} operations:")
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
