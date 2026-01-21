from pathlib import Path
from _common import run_demo

OPERATION = 'VendorGetListByLastNamePrefix'
METHOD = 'vendor_get_list_by_last_name_prefix'
REQUEST_MODEL = 'VendorGetListByLastNamePrefixRequest'
FIELD_NAMES = ['VendorLastNamePrefix']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
