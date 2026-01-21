from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerInsert'
METHOD = 'customer_insert'
REQUEST_MODEL = 'CustomerInsertRequest'
FIELD_NAMES = ['Customer']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
