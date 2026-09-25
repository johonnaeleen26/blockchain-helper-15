import logging
import sys
from typing import Optional

class BlockchainLogger:
    def __init__(self, name: str = 'blockchain-helper-15') -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, error: Exception, context: Optional[str] = None) -> None:
        error_msg = f"context: {context} | " if context else ""
        self.logger.error(f"{error_msg}type: {type(error).__name__} | message: {str(error)}")

    def safe_execute(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, ConnectionError) as e:
            self.log_error(e, context=func.__name__)
            return None
        except Exception as e:
            self.log_error(e, context="critical_failure")
            raise

logger = BlockchainLogger()