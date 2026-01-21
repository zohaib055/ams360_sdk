from pathlib import Path
from _common import run_demo

OPERATION = 'PlanTypeGetByCode'
METHOD = 'plan_type_get_by_code'
REQUEST_MODEL = 'PlanTypeGetByCodeRequest'
FIELD_NAMES = ['PlanCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
