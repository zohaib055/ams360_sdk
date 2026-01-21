from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyGetListByCustomerId'
METHOD = 'policy_get_list_by_customer_id'
REQUEST_MODEL = 'PolicyGetListByCustomerIdRequest'
FIELD_NAMES = ['CustomerId', 'PolicyStatus', 'IncludeMultiEntity', 'IncludeAccountingSubType', 'IncludeSubmissionSubType', 'IncludePolicySubType']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
