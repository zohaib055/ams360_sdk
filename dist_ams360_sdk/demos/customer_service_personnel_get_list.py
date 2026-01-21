from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerServicePersonnelGetList'
METHOD = 'customer_service_personnel_get_list'
REQUEST_MODEL = 'CustomerServicePersonnelGetListRequest'
FIELD_NAMES = ['CustomerId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
