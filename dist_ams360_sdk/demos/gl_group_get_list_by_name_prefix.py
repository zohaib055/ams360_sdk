from pathlib import Path
from _common import run_demo

OPERATION = 'GLGroupGetListByNamePrefix'
METHOD = 'gl_group_get_list_by_name_prefix'
REQUEST_MODEL = 'GLGroupGetListByNamePrefixRequest'
FIELD_NAMES = ['GLGroupNamePrefix']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
