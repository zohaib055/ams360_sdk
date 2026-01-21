from pathlib import Path
from _common import run_demo

OPERATION = 'GLGroupGetByShortName'
METHOD = 'gl_group_get_by_short_name'
REQUEST_MODEL = 'GLGroupGetByShortNameRequest'
FIELD_NAMES = ['GLGroupShortName']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
