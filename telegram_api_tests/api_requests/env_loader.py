""" This module is for getting environment variables from .env file. """

import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TEST_USER_ID = os.getenv('TEST_USER_ID')
