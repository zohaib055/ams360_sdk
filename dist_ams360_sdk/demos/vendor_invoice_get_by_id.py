from pathlib import Path
from _common import run_demo

OPERATION = 'VendorInvoiceGetById'
METHOD = 'vendor_invoice_get_by_id'
REQUEST_MODEL = 'VendorInvoiceGetByIdRequest'
FIELD_NAMES = ['VendorInvoiceId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
