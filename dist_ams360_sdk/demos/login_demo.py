import json
import sys
from pathlib import Path

SDK_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SDK_DIR))

from ams360_sdk import AMS360Client, AMS360Settings
from ams360_sdk.errors import AMS360AuthError


def main() -> None:
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
        ticket = client.ensure_ticket()
    except AMS360AuthError as exc:
        raise SystemExit(f"Login failed: {exc}")

    print(json.dumps({"ticket": ticket}, indent=2))


if __name__ == "__main__":
    main()
