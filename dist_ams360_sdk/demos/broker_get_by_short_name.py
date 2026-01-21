from pathlib import Path
from _common import run_demo

OPERATION = 'BrokerGetByShortName'
METHOD = 'broker_get_by_short_name'
REQUEST_MODEL = 'BrokerGetByShortNameRequest'
FIELD_NAMES = ['BrokerShortName']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
