from pathlib import Path
from _common import run_demo

OPERATION = 'PlanTypeGetListByCompanyCode'
METHOD = 'plan_type_get_list_by_company_code'
REQUEST_MODEL = 'PlanTypeGetListByCompanyCodeRequest'
FIELD_NAMES = ['CompanyCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
