from pathlib import Path
from _common import run_demo

OPERATION = 'GLGroupGetListByGLDepartmentCode'
METHOD = 'gl_group_get_list_by_gl_department_code'
REQUEST_MODEL = 'GLGroupGetListByGLDepartmentCodeRequest'
FIELD_NAMES = ['GLDepartmentCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
