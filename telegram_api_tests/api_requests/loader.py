import os
from dotenv import load_dotenv
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


# Get the path to the directory this file is in
BASEDIR = get_project_root()

load_dotenv(os.path.join(BASEDIR, '.env'))

TEST_USER_ID = os.getenv('TEST_USER_ID')
