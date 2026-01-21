from pathlib import Path
from _common import run_demo

OPERATION = 'ClaimGetListByCustomerId'
METHOD = 'claim_get_list_by_customer_id'
REQUEST_MODEL = 'ClaimGetListByCustomerIdRequest'
FIELD_NAMES = ['CustomerId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
