from pathlib import Path
from _common import run_demo

OPERATION = 'Login'
METHOD = 'login'
REQUEST_MODEL = 'LoginRequest'
FIELD_NAMES = ['AgencyNo', 'LoginId', 'Password', 'EmployeeCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
