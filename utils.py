import json
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class BlockchainError(Exception):
    pass

def parse_block_data(raw_data: str) -> Optional[dict]:
    try:
        if not raw_data:
            raise ValueError("empty input data")
        
        data = json.loads(raw_data)
        
        if not isinstance(data, dict):
            raise TypeError("invalid data structure format")
            
        if "block_hash" not in data:
            raise KeyError("missing required block hash")
            
        return data
    except json.JSONDecodeError as e:
        logger.error(f"failed to parse json: {e}")
    except (ValueError, TypeError, KeyError) as e:
        logger.warning(f"data validation failure: {e}")
    except Exception as e:
        logger.critical(f"unexpected system error: {e}")
    return None

def format_wei_to_eth(wei: Any) -> float:
    try:
        if wei is None:
            raise ValueError("input is null")
        
        val = int(wei)
        if val < 0:
            raise ValueError("negative value prohibited")
            
        return val / 10**18
    except (ValueError, TypeError):
        logger.error("invalid wei input conversion attempted")
        return 0.0