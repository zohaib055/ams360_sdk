from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyGet'
METHOD = 'policy_get'
REQUEST_MODEL = 'PolicyGetRequest'
FIELD_NAMES = ['PolicyId', 'TransactionEffectiveDate']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
