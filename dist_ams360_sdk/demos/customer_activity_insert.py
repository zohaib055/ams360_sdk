from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerActivityInsert'
METHOD = 'customer_activity_insert'
REQUEST_MODEL = 'CustomerActivityInsertRequest'
FIELD_NAMES = ['CustomerActivity']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
