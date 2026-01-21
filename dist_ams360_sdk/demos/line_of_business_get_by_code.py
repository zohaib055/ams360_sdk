from pathlib import Path
from _common import run_demo

OPERATION = 'LineOfBusinessGetByCode'
METHOD = 'line_of_business_get_by_code'
REQUEST_MODEL = 'LineOfBusinessGetByCodeRequest'
FIELD_NAMES = ['LineOfBusinessCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
