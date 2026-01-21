from pathlib import Path
from _common import run_demo

OPERATION = 'PersonalNoteGetList'
METHOD = 'personal_note_get_list'
REQUEST_MODEL = 'PersonalNoteGetListRequest'
FIELD_NAMES = ['DateFrom', 'DateTo', 'PurgeDateFrom', 'PurgeDateTo', 'IncludeOnlyAttachments']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
