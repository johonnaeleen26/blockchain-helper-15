import logging
import sys
from typing import Optional

class BlockchainLogger:
    def __init__(self, name: str = "blockchain-helper-15", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: Optional[Exception] = None) -> None:
        self.logger.error(msg, exc_info=exc_info)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

def get_logger(name: str = "blockchain-helper-15") -> BlockchainLogger:
    return BlockchainLogger(name)