from pathlib import Path
from _common import run_demo

OPERATION = 'CompanyGetListByNamePrefix'
METHOD = 'company_get_list_by_name_prefix'
REQUEST_MODEL = 'CompanyGetListByNamePrefixRequest'
FIELD_NAMES = ['CompanyNamePrefix']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
