import argparse
import json
import os
import sys

from .client import AMS360Client
from .generated import Generated
from .settings import AMS360Settings

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
        print("WSDL not found:", wsdl_path)
        sys.exit(1)

    settings = AMS360Settings.from_env()
    auto_login = bool(args.login or args.call)
    ams = AMS360Client.from_settings(wsdl_path=wsdl_path, settings=settings, auto_login=auto_login)
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
        if not settings.ticket and not settings.has_credentials():
            print("Missing env vars: AMS360_AGENCY_NO, AMS360_LOGIN_ID, AMS360_PASSWORD")
            sys.exit(1)

        ticket = ams.ensure_ticket()
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
