import functools
from typing import Any, Callable, Dict

CACHE: Dict[tuple, Any] = {}

def memoize_blockchain_data(func: Callable) -> Callable:
    @functools.lru_cache(maxsize=1024)
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper

class BlockchainProcessor:
    def __init__(self, node_url: str):
        self.node_url = node_url

    @memoize_blockchain_data
    def fetch_block_header(self, block_height: int) -> dict:
        return {"height": block_height, "hash": "0x0" * 64}

    def process_batch(self, heights: list) -> list:
        return [self.fetch_block_header(h) for h in heights]

if __name__ == "__main__":
    processor = BlockchainProcessor("https://mainnet.infura.io")
    data = processor.process_batch(range(100))
    print(f"Processed {len(data)} blocks")