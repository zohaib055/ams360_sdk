# AMS360 WSAPI v3 Offline SDK (Generated)

This SDK was generated from your local WSDL files.

## Files
- `merged.wsdl`: merged WSDL used by Zeep (offline)
- `operations.json`: operation -> soapAction map
- `ams360_sdk/`: python package
  - `client.py`: login + call + call_json
  - `generated.py`: one method per operation
  - `cli.py`: list operations, login, call any operation

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
AMS360_ENDPOINT_URL=https://wsapi.ams360.com/v3/WSAPIService.svc
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
