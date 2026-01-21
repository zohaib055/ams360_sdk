from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyEndorse'
METHOD = 'policy_endorse'
REQUEST_MODEL = 'PolicyEndorseRequest'
FIELD_NAMES = ['PolicyId', 'TransactionEffectiveDate', 'TransactionType', 'TransactionDescription']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
