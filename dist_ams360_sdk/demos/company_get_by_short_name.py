from pathlib import Path
from _common import run_demo

OPERATION = 'CompanyGetByShortName'
METHOD = 'company_get_by_short_name'
REQUEST_MODEL = 'CompanyGetByShortNameRequest'
FIELD_NAMES = ['CompanyShortName']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
