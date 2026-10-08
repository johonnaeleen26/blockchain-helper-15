import hashlib
import time
from typing import List, Dict, Any

class BlockchainHelper:
    def __init__(self, difficulty: int = 4):
        self.difficulty = difficulty
        self.chain: List[Dict[str, Any]] = []

    def calculate_hash(self, block: Dict[str, Any]) -> str:
        block_string = str(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_block(self, data: str) -> None:
        index = len(self.chain)
        timestamp = time.time()
        prev_hash = self.chain[-1]['hash'] if self.chain else '0'
        
        block = {
            'index': index,
            'timestamp': timestamp,
            'data': data,
            'prev_hash': prev_hash,
            'nonce': 0
        }

        while True:
            block_hash = self.calculate_hash(block)
            if block_hash[:self.difficulty] == '0' * self.difficulty:
                block['hash'] = block_hash
                break
            block['nonce'] += 1
            
        self.chain.append(block)

    def validate_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current['prev_hash'] != previous['hash']:
                return False
            if current['hash'] != self.calculate_hash({k: v for k, v in current.items() if k != 'hash'}):
                return False
        return True