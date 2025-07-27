import os

from dotenv import load_dotenv

load_dotenv(override=True)

LOG_FILE_NAME: str | None = os.getenv("LOG_FILE_NAME")