from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyGetListByPolicyNumber'
METHOD = 'policy_get_list_by_policy_number'
REQUEST_MODEL = 'PolicyGetListByPolicyNumberRequest'
FIELD_NAMES = ['PolicyNumber', 'PolicyEffectiveDate', 'PolicyExpirationDate', 'IncludeMultiEntity', 'IncludeAccountingSubType', 'IncludeSubmissionSubType', 'IncludePolicySubType']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
