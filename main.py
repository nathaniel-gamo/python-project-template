import argparse
import logging
import time
from collections.abc import Callable
from typing import Any

import src.config


def retry(max_retries: int = 3, 
          retry_interval_seconds: int = 0, 
          retry_raise_exception: bool = True) -> (Callable[..., 
                                                           Callable[..., 
                                                                    Any]]):
    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_retries + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    logging.error("An error occurred during the "
                        f"execution of main.py.\nError message: {e}")
                    if attempt >= max_retries:
                        if retry_raise_exception:
                            raise
                        return None
                    time.sleep(retry_interval_seconds)
        return wrapper
    return decorator

def _bootstrap() -> dict[str, str | None]:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="python-project-template")

    parser.add_argument("--dotenv_path",
                        type=str,
                        default="",
                        help="The file path of .env.")

    args: argparse.Namespace = parser.parse_args()

    config: dict[str, str | None] = src.config.load_config(args.dotenv_path)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=config["LOG_FILE_PATH"]
    )

    return config

def main() -> None:
    config: dict[str, str | None] = _bootstrap()

    logging.info("Running...")

    max_retries: int = int(config["MAX_RETRIES"] 
                           if config["MAX_RETRIES"] 
                           else 0)
    
    retry_interval_seconds: int = int(config["RETRY_INTERVAL_SECONDS"] 
                                      if config["RETRY_INTERVAL_SECONDS"] 
                                      else 0)
    
    retry_raise_exception: bool = True
    if config["RETRY_RAISE_EXCEPTION"]:
        retry_raise_exception = (config["RETRY_RAISE_EXCEPTION"].lower() 
                                 == "true")

    @retry(max_retries, retry_interval_seconds, retry_raise_exception)
    def run() -> None:
        return None
    
    run()
    
if __name__ == "__main__":
    main()