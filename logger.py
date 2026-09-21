import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = Path("logs/blockchain.log")
LOG_FILE.parent.mkdir(exist_ok=True)

def setup_logger(name: str = "blockchain_helper") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = RotatingFileHandler(
        LOG_FILE, 
        maxBytes=10 * 1024 * 1024, 
        backupCount=5
    )
    handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console_handler)
    
    return logger