from pathlib import Path
from _common import run_demo

OPERATION = 'CompanyGetListByType'
METHOD = 'company_get_list_by_type'
REQUEST_MODEL = 'CompanyGetListByTypeRequest'
FIELD_NAMES = ['CompanyTypes']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
