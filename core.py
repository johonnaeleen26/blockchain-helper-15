import functools
from typing import Any, Callable

class ChainProcessor:
    def __init__(self, cache_size: int = 1024):
        self.cache_size = cache_size

    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def derive_address(pubkey: bytes) -> str:
        return pubkey.hex()[:42]

    @staticmethod
    def batch_process(items: list, func: Callable) -> list:
        return [func(item) for item in items]

    def optimize_sequence(self, sequence: list[bytes]) -> list[str]:
        return [self.derive_address(item) for item in sequence]

if __name__ == '__main__':
    processor = ChainProcessor()
    test_data = [b'\x01' * 32, b'\x02' * 32, b'\x01' * 32]
    results = processor.optimize_sequence(test_data)
    print(results)