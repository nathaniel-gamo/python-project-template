import argparse
import logging

import src.config as config


def main(args: argparse.Namespace) -> None:
    pass

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"{config.LOG_FILE_NAME}"
    )

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="python-project-template")
    """
    parser.add_argument("argument_1", 
                        type=str, 
                        help="Argument 1")
    """
    args: argparse.Namespace = parser.parse_args()

    main(args)