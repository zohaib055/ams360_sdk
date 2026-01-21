from pathlib import Path
from _common import run_demo

OPERATION = 'VendorInvoiceGetListByVendor'
METHOD = 'vendor_invoice_get_list_by_vendor'
REQUEST_MODEL = 'VendorInvoiceGetListByVendorRequest'
FIELD_NAMES = ['VendorCode']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
