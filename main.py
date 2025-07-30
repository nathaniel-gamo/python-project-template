import argparse
import logging
import time
from typing import Any, Callable

import src.config as config


def retry(function: Callable[[argparse.Namespace], None]) -> Callable[..., 
                                                                      None]:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        retry_count: int = 0
        while True:
            try:
                function(*args, **kwargs)
                break
            except Exception as e:
                logging.error("An error occurred during the "
                      f"execution of main.py.\nError message: {e}")
                if retry_count >= config.MAX_RETRIES:
                    break
                retry_count += 1
                time.sleep(config.RETRY_INTERVAL_SECONDS)
    return wrapper

@retry
def main(args: argparse.Namespace) -> None:
    logging.info("Running main.py...")

if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="python-project-template")
    
    parser.add_argument("dotenv_path",
                        type=str,
                        default="",
                        nargs="?",
                        help="The file path of .env.")
    
    args: argparse.Namespace = parser.parse_args()

    if args.dotenv_path:
        config.call_load_dotenv(args.dotenv_path)
    else:
        config.call_load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"{config.LOG_FILE_PATH}"
    )

    main(args)