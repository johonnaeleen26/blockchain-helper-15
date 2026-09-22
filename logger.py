import logging
import sys
from typing import Optional

class BlockchainLogger:
    def __init__(self, name: str = "blockchain-helper-15", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: Optional[Exception] = None) -> None:
        self.logger.error(msg, exc_info=exc_info)

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

def get_logger(name: str = "blockchain-helper-15") -> logging.Logger:
    return BlockchainLogger(name).logger