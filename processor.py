import logging

class BlockchainError(Exception):
    pass

def process_transaction(tx_data: dict) -> dict:
    if not isinstance(tx_data, dict):
        raise ValueError('Invalid transaction data format')
    
    required = {'sender', 'receiver', 'amount'}
    if not required.issubset(tx_data.keys()):
        raise KeyError(f'Missing required fields: {required - tx_data.keys()}')

    try:
        amount = float(tx_data['amount'])
        if amount <= 0:
            raise ValueError('Transaction amount must be positive')
        
        return {'status': 'success', 'tx_id': hash(frozenset(tx_data.items()))}
    except (TypeError, ValueError) as e:
        logging.error(f'Processing failed: {e}')
        raise BlockchainError(f'Transaction validation failed: {e}')

def batch_process(transactions: list) -> list:
    results = []
    for tx in transactions:
        try:
            results.append(process_transaction(tx))
        except (BlockchainError, KeyError, ValueError):
            results.append({'status': 'failed'})
    return results