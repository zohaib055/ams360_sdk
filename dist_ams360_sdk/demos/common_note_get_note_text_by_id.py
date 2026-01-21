from pathlib import Path
from _common import run_demo

OPERATION = 'CommonNoteGetNoteTextById'
METHOD = 'common_note_get_note_text_by_id'
REQUEST_MODEL = None
FIELD_NAMES = []

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
