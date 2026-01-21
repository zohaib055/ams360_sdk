from pathlib import Path
from _common import run_demo

OPERATION = 'EmployeeUpdate'
METHOD = 'employee_update'
REQUEST_MODEL = 'EmployeeUpdateRequest'
FIELD_NAMES = ['Employee']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
