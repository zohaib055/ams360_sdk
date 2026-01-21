from pathlib import Path
from _common import run_demo

OPERATION = 'AMS360AgencyUrlGet'
METHOD = 'ams360_agency_url_get'
REQUEST_MODEL = None
FIELD_NAMES = []

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
