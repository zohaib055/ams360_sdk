from pathlib import Path
from _common import run_demo

OPERATION = 'GLDepartmentGetByCode'
METHOD = 'gl_department_get_by_code'
REQUEST_MODEL = 'GLDepartmentGetByCodeRequest'
FIELD_NAMES = ['GLDepartmentCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
