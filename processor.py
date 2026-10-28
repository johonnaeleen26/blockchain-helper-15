import logging
from typing import List, Dict, Optional

class BlockchainProcessor:
    def __init__(self, node_url: str, timeout: int = 30):
        self.node_url = node_url
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

    def validate_tx(self, tx: Dict) -> bool:
        return all(key in tx for key in ('hash', 'sender', 'value'))

    def process_batch(self, transactions: List[Dict]) -> List[str]:
        processed = []
        for tx in transactions:
            if self.validate_tx(tx):
                self._execute(tx)
                processed.append(tx['hash'])
            else:
                self.logger.warning(f"invalid transaction: {tx.get('hash', 'unknown')}")
        return processed

    def _execute(self, tx: Dict) -> None:
        self.logger.info(f"executing {tx['hash']}")

    @staticmethod
    def format_wei(amount: int) -> float:
        return amount / 10**18