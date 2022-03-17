import os

from configs.exceptions import StageWrongValueError

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE = os.environ.get('STAGE', 'prod')

if STAGE == 'prod':
    DOTENV_FILE_PATH = f'{BASE_PATH}\\.prod.env'
elif STAGE == 'dev':
    DOTENV_FILE_PATH = f'{BASE_PATH}\\.dev.env'
else:
    raise StageWrongValueError(stage_value=STAGE)
