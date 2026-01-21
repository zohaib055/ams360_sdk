from pathlib import Path
from _common import run_demo

OPERATION = 'PolicyCorrect'
METHOD = 'policy_correct'
REQUEST_MODEL = 'PolicyCorrectRequest'
FIELD_NAMES = ['Policy']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
