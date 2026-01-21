from pathlib import Path
from _common import run_demo

OPERATION = 'GLDivisionGetListByNamePrefix'
METHOD = 'gl_division_get_list_by_name_prefix'
REQUEST_MODEL = 'GLDivisionGetListByNamePrefixRequest'
FIELD_NAMES = ['GLDivisionNamePrefix']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
