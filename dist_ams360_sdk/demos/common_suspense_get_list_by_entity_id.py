from pathlib import Path
from _common import run_demo

OPERATION = 'CommonSuspenseGetListByEntityId'
METHOD = 'common_suspense_get_list_by_entity_id'
REQUEST_MODEL = 'CommonSuspenseGetListByEntityIdRequest'
FIELD_NAMES = ['EntityId', 'IsCompleted', 'EntityType']

if __name__ == "__main__":
    run_demo(OPERATION, METHOD, REQUEST_MODEL, FIELD_NAMES, Path(__file__).with_suffix(".json"))
