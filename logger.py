import logging
import sys
import json
from datetime import datetime, timezone

class CryptoFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module
        }
        if hasattr(record, "tx_hash"):
            log_data["tx_hash"] = getattr(record, "tx_hash")
        if hasattr(record, "block_number"):
            log_data["block_number"] = getattr(record, "block_number")
        return json.dumps(log_data)

def get_blockchain_logger(name: str = "blockchain") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(CryptoFormatter())
    logger.addHandler(handler)
    logger.propagate = False
    return logger