from pathlib import Path
from _common import run_demo

OPERATION = 'CommonSuspenseDelete'
METHOD = 'common_suspense_delete'
REQUEST_MODEL = 'CommonSuspenseDeleteRequest'
FIELD_NAMES = ['SuspenseId', 'SuspenseTypeId', 'SuspenseType']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
