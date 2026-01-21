from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerSuspenseInsert'
METHOD = 'customer_suspense_insert'
REQUEST_MODEL = 'CustomerSuspenseInsertRequest'
FIELD_NAMES = ['Suspense']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
