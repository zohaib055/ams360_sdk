from pathlib import Path
from _common import run_demo

OPERATION = 'CommonSuspenseGetBySuspenseId'
METHOD = 'common_suspense_get_by_suspense_id'
REQUEST_MODEL = 'CommonSuspenseGetBySuspenseIdRequest'
FIELD_NAMES = ['SuspenseId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
