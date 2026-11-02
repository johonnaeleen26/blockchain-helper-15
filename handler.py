import logging
from typing import Any, Optional

class BlockchainError(Exception):
    pass

class TransactionHandler:
    def __init__(self, client: Any):
        self.client = client
        self.logger = logging.getLogger(__name__)

    def execute_transaction(self, tx_data: dict) -> Optional[str]:
        if not isinstance(tx_data, dict) or not tx_data:
            self.logger.error("Invalid transaction payload")
            return None

        try:
            response = self.client.send(tx_data)
            if not response:
                raise BlockchainError("Empty response from node")
            return response.get('tx_hash')
        except ConnectionError as e:
            self.logger.error(f"Network connectivity failure: {e}")
        except TimeoutError:
            self.logger.warning("Transaction request timed out")
        except Exception as e:
            self.logger.critical(f"Unexpected blockchain error: {e}")
            raise BlockchainError("Critical failure in transmission") from e
        return None

    def validate_node_health(self) -> bool:
        try:
            return self.client.get_status().get('is_synced', False)
        except (AttributeError, KeyError):
            self.logger.error("Node status format mismatch")
            return False
        except Exception:
            return False