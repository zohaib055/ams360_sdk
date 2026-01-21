from pathlib import Path
from _common import run_demo

OPERATION = 'CustomerNoteInsert'
METHOD = 'customer_note_insert'
REQUEST_MODEL = 'CustomerNoteInsertRequest'
FIELD_NAMES = ['CustomerNote']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
