from pathlib import Path
from _common import run_demo

OPERATION = 'VendorGetListByIsCompany'
METHOD = 'vendor_get_list_by_is_company'
REQUEST_MODEL = 'VendorGetListByIsCompanyRequest'
FIELD_NAMES = ['IsCompany']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
