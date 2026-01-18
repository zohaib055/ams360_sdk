import argparse
from .client import AMS360Client

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--list-ops", action="store_true")
    p.add_argument("--agency-info", action="store_true")
    args = p.parse_args()

    ams = AMS360Client.from_env()

    if args.list_ops:
        # list ops from zeep
        ops = []
        for service in ams.soap.client.wsdl.services.values():
            for port in service.ports.values():
                for op in port.binding._operations.keys():
                    ops.append(op)
        for op in sorted(set(ops)):
            print(op)
        return

    if args.agency_info:
        ams.login()
        print(ams.agency.get_info())
        return

    p.print_help()

if __name__ == "__main__":
    main()
