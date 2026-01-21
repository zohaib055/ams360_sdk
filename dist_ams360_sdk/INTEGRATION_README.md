# AMS360 SDK Integration Guide

This guide shows how to configure authentication, use the SDK in a production-style integration,
and view JSON payload/response examples for common customer methods.

## Settings and setup

The SDK uses `AMS360Settings` to hold all authentication settings. You can provide a ticket
directly or supply credentials so the SDK logs in and reuses the ticket for all calls.

```python
from ams360_sdk import AMS360Client, AMS360Settings, Generated

settings = AMS360Settings(
    agency_no="8880006-1",
    login_id="myuser",
    password="mypassword",
    employee_code="",
    endpoint_url="https://wsapi.ams360.com/v3/WSAPIService.svc",
    verify_tls=True,
    timeout=60,
    operation_timeout=120,
    ticket=None,  # optional: reuse an existing ticket
)

client = AMS360Client.from_settings(
    settings=settings,
    auto_login=True,
)
gen = Generated(client)
```

You can also load settings from environment variables:

```python
settings = AMS360Settings.from_env()
```

Environment variables supported:

- `AMS360_AGENCY_NO`
- `AMS360_LOGIN_ID`
- `AMS360_PASSWORD`
- `AMS360_EMPLOYEE_CODE` (optional)
- `AMS360_TICKET` (optional, skip login if already available)
- `AMS360_ENDPOINT_URL`
- `AMS360_VERIFY_TLS` (true/false)
- `AMS360_TIMEOUT`
- `AMS360_OPERATION_TIMEOUT`

## Authentication flow

1) Provide a ticket (recommended if your app caches it)

```python
settings = AMS360Settings.from_env()
settings.ticket = "existing-ticket"
client = AMS360Client.from_settings(settings=settings, auto_login=False)
```

2) Provide credentials (SDK logs in and stores the ticket internally)

```python
settings = AMS360Settings.from_env()
client = AMS360Client.from_settings(settings=settings, auto_login=True)
client.ensure_ticket()
```

## JSON responses

Use the `*_json` method variants to get Python dicts/lists (JSON-ready).
If you need a JSON string, call `json.dumps(result)`.

## WSDL handling

`AMS360Client` automatically locates `merged.wsdl` next to the `ams360_sdk` package
(the parent folder of `ams360_sdk`). Pass `wsdl_path` only if you need to override it.

## Demos

The `demos/` folder contains one script per operation. Each script prints JSON output.
For request-based operations, supply a JSON payload using:

- `AMS360_DEMO_PAYLOAD_JSON` (JSON string), or
- `AMS360_DEMO_PAYLOAD_FILE` (path to a JSON file), or
- a `.json` file next to the demo script with the same name.

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

## Method payload and response examples

Below are common customer methods. For the full list, see `operations.json` or
`ams360_sdk/generated.py`. All methods follow the same pattern: pass a request model
from `ams360_sdk/models.py` and call the `*_json` method.

### Customer list by name prefix (CustomerGetListByNamePrefix)

Payload:

```python
from ams360_sdk import models

request = models.CustomerGetListByNamePrefixRequest(NamePrefix="A")
result = gen.customer_get_list_by_name_prefix_json(request=request)
```

Response (example):

```json
{
  "CustomerGetListByNamePrefixResult": {
    "CustomerInfoList": {
      "CustomerInfo": [
        {
          "CustomerId": "4491edb1-3d68-468b-8adc-0d41c04a25e9",
          "CustomerNumber": 5544,
          "FirstName": "Kent",
          "LastName": "Anthony",
          "FirmName": null,
          "IsActive": false
        }
      ]
    }
  }
}
```

### Customer lookup by number (CustomerGetByNumber)

Payload:

```python
request = models.CustomerGetByNumberRequest(CustomerNumber="5544")
result = gen.customer_get_by_number_json(request=request)
```

Response (example):

```json
{
  "CustomerGetByNumberResult": {
    "Customer": {
      "CustomerId": "4491edb1-3d68-468b-8adc-0d41c04a25e9",
      "CustomerNumber": 5544,
      "FirstName": "Kent",
      "LastName": "Anthony"
    }
  }
}
```

### Customer search by phone (SearchByPhoneNumber)

Payload:

```python
request = models.SearchByPhoneNumberRequest(PhoneNumber="5551234567")
result = gen.search_by_phone_number_json(request=request)
```

Response (example):

```json
{
  "SearchByPhoneNumberResult": {
    "SearchResults": {
      "SearchResult": [
        {
          "EntityId": "4491edb1-3d68-468b-8adc-0d41c04a25e9",
          "EntityType": "Customer",
          "DisplayName": "Kent Anthony"
        }
      ]
    }
  }
}
```
