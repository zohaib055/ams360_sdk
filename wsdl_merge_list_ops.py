import argparse
import json
import os
from pathlib import Path

import requests
from lxml import etree
from zeep import Client, Settings
from zeep.transports import Transport


WSDL_NS = {"wsdl": "http://schemas.xmlsoap.org/wsdl/"}


def merge_wsdl(service_wsdl: Path, contract_wsdl: Path, out_wsdl: Path) -> Path:
    """
    Merges:
      - binding (from WSAPIService.wsdl)
      - into contract WSDL (WSAPIServiceContract.wsdl) which already has service + portType + types/messages

    Writes merged WSDL to out_wsdl.
    """
    svc_doc = etree.parse(str(service_wsdl))
    ctr_doc = etree.parse(str(contract_wsdl))

    svc_defs = svc_doc.getroot()
    ctr_defs = ctr_doc.getroot()

    # Grab binding from service wsdl
    svc_bindings = svc_doc.xpath("/wsdl:definitions/wsdl:binding", namespaces=WSDL_NS)
    if not svc_bindings:
        raise RuntimeError(f"No wsdl:binding found in {service_wsdl}")

    # If contract already has binding(s), don't duplicate
    ctr_bindings = ctr_doc.xpath("/wsdl:definitions/wsdl:binding", namespaces=WSDL_NS)
    if ctr_bindings:
        print("Contract WSDL already has bindings; skipping merge of bindings.")
    else:
        # Append binding(s) into contract definitions
        for b in svc_bindings:
            ctr_defs.append(b)

    out_wsdl.write_bytes(etree.tostring(ctr_doc, pretty_print=True, xml_declaration=True, encoding="utf-8"))
    return out_wsdl


def list_ops_with_zeep(wsdl_path: Path):
    session = requests.Session()
    transport = Transport(session=session, timeout=60, operation_timeout=120)
    settings = Settings(strict=False, xml_huge_tree=True)

    wsdl_abs = str(wsdl_path.resolve())  # <-- key fix for Windows
    client = Client(wsdl=wsdl_abs, transport=transport, settings=settings)

    ops = []
    for service in client.wsdl.services.values():
        for port in service.ports.values():
            for op_name in port.binding._operations.keys():
                ops.append(op_name)

    return sorted(set(ops))



def extract_soap_actions(wsdl_path: Path):
    """
    Optional: extract operation -> soapAction mapping from merged WSDL binding.
    """
    doc = etree.parse(str(wsdl_path))
    root = doc.getroot()

    # SOAP 1.1 operation element is soap:operation under wsdl:operation
    ns = {
        "wsdl": "http://schemas.xmlsoap.org/wsdl/",
        "soap": "http://schemas.xmlsoap.org/wsdl/soap/",
    }

    mapping = {}
    for op in doc.xpath("//wsdl:binding/wsdl:operation", namespaces=ns):
        name = op.get("name")
        soap_op = op.find("soap:operation", namespaces=ns)
        action = soap_op.get("soapAction") if soap_op is not None else None
        if name:
            mapping[name] = action
    return mapping


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--service-wsdl", default="WSAPIService.wsdl", help="Path to WSAPIService.wsdl")
    p.add_argument("--contract-wsdl", default="WSAPIServiceContract.wsdl", help="Path to WSAPIServiceContract.wsdl")
    p.add_argument("--out-wsdl", default="merged.wsdl", help="Output merged WSDL filename")
    p.add_argument("--write-actions-json", action="store_true", help="Write operations + soapAction to operations.json")
    args = p.parse_args()

    service_wsdl = Path(args.service_wsdl)
    contract_wsdl = Path(args.contract_wsdl)
    out_wsdl = Path(args.out_wsdl)

    if not service_wsdl.exists():
        raise SystemExit(f"Missing file: {service_wsdl}")
    if not contract_wsdl.exists():
        raise SystemExit(f"Missing file: {contract_wsdl}")

    merged = merge_wsdl(service_wsdl, contract_wsdl, out_wsdl)
    print(f"✅ Merged WSDL written to: {merged}")

    ops = list_ops_with_zeep(merged)
    print(f"\nFound {len(ops)} operations:\n")
    for op in ops:
        print(op)

    if args.write_actions_json:
        actions = extract_soap_actions(merged)
        out = []
        for op in ops:
            out.append({"operation": op, "soapAction": actions.get(op)})
        Path("operations.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
        print("\n✅ Wrote operations.json (operation -> soapAction)")


if __name__ == "__main__":
    main()
