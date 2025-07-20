import os

from dotenv import load_dotenv

load_dotenv()

LOG_FILE_NAME: str | None = os.getenv("LOG_FILE_NAME")