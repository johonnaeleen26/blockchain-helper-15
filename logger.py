import logging
import sys
from typing import Optional

class BlockchainLogger:
    def __init__(self, name: str = "blockchain-helper-15"):
        self.logger = logging.getLogger(name)
        self._configure()

    def _configure(self) -> None:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        if not isinstance(message, str) or not message:
            return
        
        error_details = f": {str(exc)}" if exc else ""
        try:
            self.logger.error(f"{message}{error_details}")
        except (ValueError, TypeError):
            sys.stderr.write(f"critical error in logger: {message}\n")

    def log_event(self, event: str) -> None:
        try:
            self.logger.info(str(event))
        except Exception:
            pass

logger = BlockchainLogger()