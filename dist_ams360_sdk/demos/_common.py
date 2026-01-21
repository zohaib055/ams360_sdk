import json
import os
import re
import sys
from pathlib import Path
from typing import Optional

SDK_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SDK_DIR))

from ams360_sdk import AMS360Client, AMS360Settings, Generated, models
from ams360_sdk.errors import AMS360AuthError

def _load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")

def load_payload(payload_path: Path, field_names: list[str]) -> dict:
    env_json = os.getenv("AMS360_DEMO_PAYLOAD_JSON", "")
    if env_json:
        try:
            return json.loads(env_json)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid AMS360_DEMO_PAYLOAD_JSON: {exc}")

    payload_file = os.getenv("AMS360_DEMO_PAYLOAD_FILE", "")
    if payload_file:
        return _load_json(Path(payload_file))

    if payload_path.exists():
        return _load_json(payload_path)

    if field_names:
        fields = ", ".join(field_names)
        raise SystemExit(
            "Missing payload JSON. Provide AMS360_DEMO_PAYLOAD_JSON "
            f"or create {payload_path} with fields: {fields}"
        )

    return {}

def _mask_secret(xml_text: str, tag: str) -> str:
    if not xml_text:
        return xml_text
    pattern = rf"(<{tag}>)(.*?)(</{tag}>)"
    return re.sub(pattern, r"\1***\3", xml_text, flags=re.DOTALL)

def _write_login_soap(client: AMS360Client) -> Optional[str]:
    soap = client.last_login_soap()
    if not soap.get("request") and not soap.get("response"):
        return None
    out_dir = Path(__file__).resolve().parent
    req_path = out_dir / "login_request.xml"
    resp_path = out_dir / "login_response.xml"
    request_xml = _mask_secret(soap.get("request", ""), "a:Password")
    response_xml = _mask_secret(soap.get("response", ""), "Ticket")
    req_path.write_text(request_xml, encoding="utf-8")
    resp_path.write_text(response_xml, encoding="utf-8")
    return str(out_dir)

def get_gen() -> Generated:
    client = AMS360Client.from_env(auto_login=False)
    settings = client.settings or AMS360Settings.from_env()
    if not settings.ticket and not settings.has_credentials():
        raise SystemExit(
            "Missing credentials. Set AMS360_AGENCY_NO, AMS360_LOGIN_ID, "
            "AMS360_PASSWORD or AMS360_TICKET."
        )
    try:
        if client.settings is None:
            client.configure_auth(settings, auto_login=True)
        else:
            client.configure_auth(client.settings, auto_login=True)
        client.ensure_ticket()
    except AMS360AuthError as exc:
        location = _write_login_soap(client)
        detail = f" Wrote login SOAP to {location}." if location else ""
        raise SystemExit(f"Login failed: {exc}.{detail}")
    return Generated(client)

def run_demo(
    operation: str,
    method_name: str,
    request_model: Optional[str],
    field_names: list[str],
    payload_path: Path,
) -> None:
    gen = get_gen()
    if request_model:
        payload = load_payload(payload_path, field_names)
        model_cls = getattr(models, request_model, None)
        if model_cls:
            request = model_cls(**payload)
        else:
            request = payload
        result = getattr(gen, f"{method_name}_json")(request=request)
    else:
        result = getattr(gen, f"{method_name}_json")()

    print(json.dumps(result, indent=2))
