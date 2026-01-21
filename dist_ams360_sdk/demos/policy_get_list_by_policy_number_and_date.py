from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyGetListByPolicyNumberAndDate'
METHOD = 'policy_get_list_by_policy_number_and_date'
REQUEST_MODEL = 'PolicyGetListByPolicyNumberAndDateRequest'
FIELD_NAMES = ['PolicyNumber', 'InEffectOnDate', 'IncludeMultiEntity', 'IncludeAccountingSubType', 'IncludeSubmissionSubType', 'IncludePolicySubType']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
