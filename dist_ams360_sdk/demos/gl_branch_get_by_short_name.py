from pathlib import Path
from _common import run_demo

OPERATION = 'GLBranchGetByShortName'
METHOD = 'gl_branch_get_by_short_name'
REQUEST_MODEL = 'GLBranchGetByShortNameRequest'
FIELD_NAMES = ['GLBranchShortName']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
