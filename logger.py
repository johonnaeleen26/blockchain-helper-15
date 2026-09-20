import logging
import sys
from typing import Optional

class BlockchainLogger:
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc: Optional[Exception] = None) -> None:
        self.logger.error(msg, exc_info=exc)

def get_logger(name: str) -> BlockchainLogger:
    return BlockchainLogger(name)