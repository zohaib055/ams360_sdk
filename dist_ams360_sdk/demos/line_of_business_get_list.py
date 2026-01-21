from pathlib import Path
from _common import run_demo

OPERATION = 'LineOfBusinessGetList'
METHOD = 'line_of_business_get_list'
REQUEST_MODEL = 'LineOfBusinessGetListRequest'
FIELD_NAMES = ['TypeOfBusinessCode', 'IncomeGroup']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
