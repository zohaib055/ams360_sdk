# AMS360 WSAPI v3 Offline SDK (Generated)

This SDK was generated from your local WSDL files.

## Files
- `merged.wsdl`: merged WSDL used by Zeep (offline)
- `operations.json`: operation -> soapAction map
- `ams360_sdk/`: python package
  - `client.py`: auth + call + call_json
  - `generated.py`: one method per operation
  - `cli.py`: list operations, login, call any operation
- `demos/`: one demo script per operation
- `INTEGRATION_README.md`: settings, auth flow, payload/response examples

## Install deps
```bash
pip install zeep requests lxml
```

## Environment variables
```bash
AMS360_AGENCY_NO=8880006-1
AMS360_LOGIN_ID=testuser
AMS360_PASSWORD=...
AMS360_EMPLOYEE_CODE=   # optional if "Specific Employee = WSAPI" mapping is set
AMS360_TICKET=          # optional: reuse an existing ticket
AMS360_ENDPOINT_URL=https://wsapi.ams360.com/v3/WSAPIService.svc
AMS360_VERIFY_TLS=true
AMS360_TIMEOUT=60
AMS360_OPERATION_TIMEOUT=120
```

## WSDL handling
`AMS360Client` automatically looks for `merged.wsdl` next to the `ams360_sdk` package
(the parent folder of `ams360_sdk`). Pass `wsdl_path` only if you want to override it.

## Demos
Each script in `demos/` runs a single operation and prints JSON output.
For operations that require a request, provide JSON payload via:

- `AMS360_DEMO_PAYLOAD_JSON` (JSON string), or
- `AMS360_DEMO_PAYLOAD_FILE` (path to a JSON file), or
- a file next to the demo script with the same name and `.json` extension.

Example:
```bash
python demos/customer_get_list_by_name_prefix.py
```

Login demo (prints the ticket as JSON):
```bash
python demos/login_demo.py
```

End-to-end demo (login, print ticket, then run AgencyInfoGet):
```bash
python ..\demo.py
```

## Run CLI (list operations)
From the output folder:
```bash
python -m ams360_sdk.cli --list-ops
```

## Login + call AgencyInfoGet
```bash
python -m ams360_sdk.cli --login --call AgencyInfoGet --json --payload "{}"
```
