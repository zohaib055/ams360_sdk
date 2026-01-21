from pathlib import Path
from _common import run_demo

OPERATION = 'GLBranchGetListByNamePrefix'
METHOD = 'gl_branch_get_list_by_name_prefix'
REQUEST_MODEL = 'GLBranchGetListByNamePrefixRequest'
FIELD_NAMES = ['GLBranchNamePrefix']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
