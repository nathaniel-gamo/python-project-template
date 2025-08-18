import os
import sys

from dotenv import load_dotenv

LOG_FILE_PATH: str = ""
MAX_RETRIES: int = 0
RETRY_INTERVAL_SECONDS: int = 0

_basedir: str
if getattr(sys, "frozen", False):
    _basedir = os.path.dirname(sys.executable)
else:
    _basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_dotenv_path: str = os.path.join(_basedir, ".env")

def call_load_dotenv(dotenv_path: str) -> None:
    global LOG_FILE_PATH
    global MAX_RETRIES
    global RETRY_INTERVAL_SECONDS

    load_dotenv(dotenv_path=dotenv_path if os.path.isfile(dotenv_path) 
                else _dotenv_path, override=True)

    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "app.log")
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "0"))
    RETRY_INTERVAL_SECONDS = int(os.getenv("RETRY_INTERVAL_SECONDS", "0"))