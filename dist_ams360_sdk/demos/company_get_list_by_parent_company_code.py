from pathlib import Path
from _common import run_demo

OPERATION = 'CompanyGetListByParentCompanyCode'
METHOD = 'company_get_list_by_parent_company_code'
REQUEST_MODEL = 'CompanyGetListByParentCompanyCodeRequest'
FIELD_NAMES = ['ParentCompanyCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
