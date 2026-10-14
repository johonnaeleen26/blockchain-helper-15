import logging
import sys
from typing import Optional


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_exception(logger: logging.Logger, exc: Exception, context: Optional[str] = None) -> None:
    msg = f"Context: {context} | " if context else ""
    logger.error(f"{msg}Exception occurred: {type(exc).__name__} - {str(exc)}")