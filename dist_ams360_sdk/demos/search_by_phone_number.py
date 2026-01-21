from pathlib import Path
from _common import run_demo

OPERATION = 'SearchByPhoneNumber'
METHOD = 'search_by_phone_number'
REQUEST_MODEL = 'SearchByPhoneNumberRequest'
FIELD_NAMES = ['PhoneNumber']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
