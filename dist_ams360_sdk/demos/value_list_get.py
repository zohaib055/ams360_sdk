from pathlib import Path
from _common import run_demo

OPERATION = 'ValueListGet'
METHOD = 'value_list_get'
REQUEST_MODEL = 'ValueListGetRequest'
FIELD_NAMES = ['ListName']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
