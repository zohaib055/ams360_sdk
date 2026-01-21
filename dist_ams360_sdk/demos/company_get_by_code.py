from pathlib import Path
from _common import run_demo

OPERATION = 'CompanyGetByCode'
METHOD = 'company_get_by_code'
REQUEST_MODEL = 'CompanyGetByCodeRequest'
FIELD_NAMES = ['CompanyCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
