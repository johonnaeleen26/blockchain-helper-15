import functools
from typing import Dict, Any, Optional

CACHE_SIZE = 1024

class ChainProcessor:
    def __init__(self, node_url: str):
        self.node_url = node_url
        self._memo = {}

    @functools.lru_cache(maxsize=CACHE_SIZE)
    def fetch_block_data(self, block_height: int) -> Dict[str, Any]:
        # Simulation of expensive blockchain rpc call
        return {"height": block_height, "hash": f"0x{'a' * 64}"}

    def process_batch(self, heights: list[int]) -> list[Dict[str, Any]]:
        return [self.fetch_block_data(h) for h in heights]

    def clear_cache(self):
        self.fetch_block_data.cache_clear()

class TransactionSigner:
    def __init__(self):
        self._tx_buffer = []

    def add_to_buffer(self, tx: Dict[str, Any]) -> None:
        if len(self._tx_buffer) < 500:
            self._tx_buffer.append(tx)

    def flush_buffer(self) -> list[Dict[str, Any]]:
        batch = list(self._tx_buffer)
        self._tx_buffer.clear()
        return batch