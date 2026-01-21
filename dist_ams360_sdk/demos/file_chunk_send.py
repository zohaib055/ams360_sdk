from pathlib import Path
from _common import run_demo

OPERATION = 'FileChunkSend'
METHOD = 'file_chunk_send'
REQUEST_MODEL = 'FileChunkSendRequest'
FIELD_NAMES = ['FileChunk']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
