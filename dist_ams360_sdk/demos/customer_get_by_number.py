from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerGetByNumber'
METHOD = 'customer_get_by_number'
REQUEST_MODEL = 'CustomerGetByNumberRequest'
FIELD_NAMES = ['CustomerNumber']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
