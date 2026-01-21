from pathlib import Path
from _common import run_demo

OPERATION = 'GLDepartmentGetListByNamePrefix'
METHOD = 'gl_department_get_list_by_name_prefix'
REQUEST_MODEL = 'GLDepartmentGetListByNamePrefixRequest'
FIELD_NAMES = ['GLDepartmentNamePrefix']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
