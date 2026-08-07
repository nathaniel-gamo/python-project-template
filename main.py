import argparse
import logging
import sys
import time
from collections.abc import Callable
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s %(levelname)s "
        "[%(message)s] %(filename)s "
        "| %(funcName)s | %(lineno)d"),
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("app.log"), 
              logging.StreamHandler(sys.stdout)])

import src.config

logger: logging.Logger = logging.getLogger(__name__)


def retry(max_retries: int, 
          retry_interval_seconds: int, 
          retry_raise_exception: bool) -> Callable[..., Callable[..., Any]]:
    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_retries + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    logger.error(f"An exception occurred. Message: {e}")
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

    parser.add_argument(
        "--dotenv_path", 
        type=str, 
        default="", 
        help="The file path of .env.")

    args: argparse.Namespace = parser.parse_args()

    config: dict[str, str | None] = src.config.load_config(args.dotenv_path)

    return config


def main() -> None:
    logger.info("Running...")

    config: dict[str, str | None] = _bootstrap()

    max_retries: int = int(config.get("MAX_RETRIES") or 0)
    retry_interval_seconds: int = int(config.get("RETRY_INTERVAL_SECONDS") 
                                      or 0)
    retry_raise_exception: bool = config.get("RETRY_RAISE_EXCEPTION", 
                                             "True") in ["True", "true"]

    @retry(max_retries, retry_interval_seconds, retry_raise_exception)
    def run() -> None:
        return None

    run()


if __name__ == "__main__":
    main()
