from pathlib import Path
from _common import run_demo

OPERATION = 'BankGetListByAccountType'
METHOD = 'bank_get_list_by_account_type'
REQUEST_MODEL = None
FIELD_NAMES = []

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
