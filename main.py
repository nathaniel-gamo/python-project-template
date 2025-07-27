import argparse
import logging

import src.config as config


def main(args: argparse.Namespace) -> None:
    try:
        logging.info("Executing main.py...")
    except Exception as e:
        logging.error("An error occurred during the "
                      f"execution of main.py.\nError message: {e}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"{config.LOG_FILE_PATH}"
    )

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="python-project-template")
    """
    parser.add_argument("argument_1", 
                        default=None, 
                        nargs="?", 
                        type=str, 
                        help="argument 1")
    """
    args: argparse.Namespace = parser.parse_args()

    main(args)