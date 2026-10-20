import logging
from typing import Any, Dict, Optional

class BlockchainProcessor:
    def __init__(self, chain_id: int):
        self.chain_id = chain_id
        self.logger = logging.getLogger(__name__)

    def validate_payload(self, data: Dict[str, Any]) -> bool:
        required = {'tx_hash', 'amount', 'sender'}
        if not all(key in data for key in required):
            self.logger.error('missing required transaction fields')
            return False
        if data['amount'] <= 0:
            self.logger.error('invalid transaction amount')
            return False
        return True

    def process_transaction(self, data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if not data:
            raise ValueError('empty transaction payload')
        
        try:
            if not self.validate_payload(data):
                return {'status': 'rejected', 'reason': 'validation_failed'}
            
            return {'status': 'confirmed', 'tx_hash': data['tx_hash']}
        except KeyError as e:
            self.logger.exception(f'malformed transaction data: {e}')
            return {'status': 'error', 'reason': 'malformed_data'}
        except Exception as e:
            self.logger.critical(f'unexpected processing failure: {e}')
            return {'status': 'failed', 'reason': 'internal_error'}