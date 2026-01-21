from pathlib import Path
from _common import run_demo

OPERATION = 'FileChunkBegin'
METHOD = 'file_chunk_begin'
REQUEST_MODEL = 'FileChunkBeginRequest'
FIELD_NAMES = ['NumberOfChunks', 'TotalBytes']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
