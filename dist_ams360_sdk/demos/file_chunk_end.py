from pathlib import Path
from _common import run_demo

OPERATION = 'FileChunkEnd'
METHOD = 'file_chunk_end'
REQUEST_MODEL = 'FileChunkEndRequest'
FIELD_NAMES = ['DocStageId']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
