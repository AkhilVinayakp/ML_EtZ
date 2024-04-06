# logger.py
import logging
from colorama import Fore, Style


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        f'{Fore.BLUE}[%(asctime)s] %(levelname)s - %(message)s{Style.RESET_ALL}'
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


# Create and configure the logger
logger = setup_logger()
