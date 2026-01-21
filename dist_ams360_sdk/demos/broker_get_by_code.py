from pathlib import Path
from _common import run_demo

OPERATION = 'BrokerGetByCode'
METHOD = 'broker_get_by_code'
REQUEST_MODEL = 'BrokerGetByCodeRequest'
FIELD_NAMES = ['BrokerCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
