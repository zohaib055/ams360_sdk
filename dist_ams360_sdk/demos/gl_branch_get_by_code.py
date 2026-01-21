from pathlib import Path
from _common import run_demo

OPERATION = 'GLBranchGetByCode'
METHOD = 'gl_branch_get_by_code'
REQUEST_MODEL = 'GLBranchGetByCodeRequest'
FIELD_NAMES = ['GLBranchCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
