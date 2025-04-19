import logging

import config

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"{config.LOG_FILE_NAME}"
    )

    logging.info("test")

if __name__ == "__main__":
    main()