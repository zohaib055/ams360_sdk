from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyGetListByCustomerNumber'
METHOD = 'policy_get_list_by_customer_number'
REQUEST_MODEL = 'PolicyGetListByCustomerNumberRequest'
FIELD_NAMES = ['CustomerNumber', 'PolicyStatus', 'IncludeMultiEntity', 'IncludeAccountingSubType', 'IncludeSubmissionSubType', 'IncludePolicySubType']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
