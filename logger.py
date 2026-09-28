import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = "blockchain.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def setup_logger(name: str = "blockchain_helper") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_path = Path(LOG_FILE)
    file_handler = RotatingFileHandler(
        log_path, 
        maxBytes=MAX_BYTES, 
        backup_count=BACKUP_COUNT
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger