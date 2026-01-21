import json
import logging
import os
import subprocess
import sys
from pathlib import Path

SDK_DIR = Path(__file__).resolve().parent / "dist_ams360_sdk"
sys.path.insert(0, str(SDK_DIR))

from ams360_sdk import AMS360Client, AMS360Settings
from ams360_sdk.errors import AMS360AuthError

LOGGER = logging.getLogger("ams360_demo")

def main() -> None:
    logging.basicConfig(
        level=os.getenv("AMS360_LOG_LEVEL", "INFO").upper(),
        format="%(asctime)s %(levelname)s %(message)s",
    )

    # Optional: set credentials here if you don't want to use env vars.
    agency_no = "8880006-1"
    login_id = "testuser"
    password = "wK1atfrjjY7"
    employee_code = ""
    ticket_override = ""

    settings = AMS360Settings.from_env()
    if agency_no:
        settings.agency_no = agency_no
    if login_id:
        settings.login_id = login_id
    if password:
        settings.password = password
    if employee_code:
        settings.employee_code = employee_code
    if ticket_override:
        settings.ticket = ticket_override

    if not settings.ticket and not settings.has_credentials():
        print(
            "Missing credentials. Set AMS360_AGENCY_NO, AMS360_LOGIN_ID, "
            "AMS360_PASSWORD or AMS360_TICKET (or fill the placeholders in demo.py)."
        )
        sys.exit(1)

    try:
        LOGGER.info("Logging in to AMS360")
        client = AMS360Client.from_settings(settings=settings, auto_login=True)
        ticket = client.ensure_ticket()
        LOGGER.info("Login succeeded; ticket received")
    except (FileNotFoundError, AMS360AuthError) as exc:
        LOGGER.error("Login failed: %s", exc)
        print(f"Login failed: {exc}")
        sys.exit(1)

    print(json.dumps({"ticket": ticket}, indent=2))

    env = os.environ.copy()
    env["AMS360_TICKET"] = ticket
    demo_path = SDK_DIR / "demos" / "agency_info_get.py"
    LOGGER.info("Running demo: %s", demo_path)
    result = subprocess.run([sys.executable, str(demo_path)], env=env)
    if result.returncode != 0:
        LOGGER.error("Demo failed with exit code %s", result.returncode)
        sys.exit(result.returncode)
    LOGGER.info("Demo finished successfully")


if __name__ == "__main__":
    main()
