from pathlib import Path
from _common import run_demo

OPERATION = 'GLDivisionGetByShortName'
METHOD = 'gl_division_get_by_short_name'
REQUEST_MODEL = 'GLDivisionGetByShortNameRequest'
FIELD_NAMES = ['GLDivisionShortName']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
