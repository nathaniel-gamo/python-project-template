import os

from dotenv import load_dotenv

load_dotenv()

LOG_FILE_NAME: str = os.environ.get("LOG_FILE_NAME")