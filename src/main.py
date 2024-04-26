import logging
import os

import numpy as np
from dotenv import load_dotenv

from logging_conf import setup_logging
from utils import load_config

load_dotenv()
CONFIG_PATH = os.getenv("CONFIG_PATH")


def main():
    # Setup Logging
    setup_logging()
    logger = logging.getLogger(__name__)

    # Load Config
    logger.info("Loading config yaml file")
    config = load_config(CONFIG_PATH)

    print(config["directory"])


if __name__ == "__main__":
    main()
