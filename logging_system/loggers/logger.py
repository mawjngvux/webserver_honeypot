# Core logger

import logging
from config.config import Config

def honeypot_web_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.HONEYPOT_WEB_SERVER_LOG_FILE),
            logging.StreamHandler()
        ]
    )

