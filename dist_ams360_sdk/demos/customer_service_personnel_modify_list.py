from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerServicePersonnelModifyList'
METHOD = 'customer_service_personnel_modify_list'
REQUEST_MODEL = 'CustomerServicePersonnelModifyListRequest'
FIELD_NAMES = ['CustomerId', 'ModifyList', 'DeleteList']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
