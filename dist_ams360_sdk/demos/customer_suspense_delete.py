from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerSuspenseDelete'
METHOD = 'customer_suspense_delete'
REQUEST_MODEL = 'CustomerSuspenseDeleteRequest'
FIELD_NAMES = ['SuspenseId', 'CustomerId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
