import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name: str = 'blockchain-helper-15', log_file: str = 'app.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_path = Path(log_file)
    handler = RotatingFileHandler(
        log_path,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding='utf-8'
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger