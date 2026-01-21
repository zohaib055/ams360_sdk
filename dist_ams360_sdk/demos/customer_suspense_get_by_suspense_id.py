from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerSuspenseGetBySuspenseId'
METHOD = 'customer_suspense_get_by_suspense_id'
REQUEST_MODEL = 'CustomerSuspenseGetBySuspenseIdRequest'
FIELD_NAMES = ['SuspenseId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
