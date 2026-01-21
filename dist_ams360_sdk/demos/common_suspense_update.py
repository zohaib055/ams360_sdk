from pathlib import Path
from _common import run_demo

OPERATION = 'CommonSuspenseUpdate'
METHOD = 'common_suspense_update'
REQUEST_MODEL = 'CommonSuspenseUpdateRequest'
FIELD_NAMES = ['CommonSuspense']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
