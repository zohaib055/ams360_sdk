from pathlib import Path
from _common import run_demo

OPERATION = 'PersonalNoteInsert'
METHOD = 'personal_note_insert'
REQUEST_MODEL = 'PersonalNoteInsertRequest'
FIELD_NAMES = ['UserNote']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
