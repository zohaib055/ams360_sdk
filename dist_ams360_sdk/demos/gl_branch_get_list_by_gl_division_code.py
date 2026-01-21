from pathlib import Path
from _common import run_demo

OPERATION = 'GLBranchGetListByGLDivisionCode'
METHOD = 'gl_branch_get_list_by_gl_division_code'
REQUEST_MODEL = 'GLBranchGetListByGLDivisionCodeRequest'
FIELD_NAMES = ['GLDivisionCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
