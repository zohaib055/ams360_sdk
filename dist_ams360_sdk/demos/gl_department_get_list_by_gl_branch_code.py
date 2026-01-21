from pathlib import Path
from _common import run_demo

OPERATION = 'GLDepartmentGetListByGLBranchCode'
METHOD = 'gl_department_get_list_by_gl_branch_code'
REQUEST_MODEL = 'GLDepartmentGetListByGLBranchCodeRequest'
FIELD_NAMES = ['GLBranchCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
