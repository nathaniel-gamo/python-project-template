import os
import sys

from dotenv import dotenv_values, load_dotenv


def _get_dotenv_path() -> str:
    if getattr(sys, "frozen", False):
        return os.path.join(os.path.dirname(sys.executable), ".env")
    
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
        ".env")

def load_config(dotenv_path: str = "", 
                dotenv_only: bool = True) -> dict[str, str | None]:
    
    if dotenv_only:
        return dotenv_values(dotenv_path=dotenv_path 
                             if os.path.isfile(dotenv_path) 
                             else _get_dotenv_path())

    load_dotenv(dotenv_path=dotenv_path 
                if os.path.isfile(dotenv_path) 
                else _get_dotenv_path(), 
                override=True)

    return {key: value for key, value in os.environ.items()}