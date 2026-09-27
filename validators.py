import re

def is_valid_ethereum_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[0-9a-fA-F]{40}$", address))

def is_valid_bitcoin_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    legacy_p2sh = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    bech32 = r"^bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39,59}$"
    return bool(re.match(legacy_p2sh, address)) or bool(re.match(bech32, address.lower()))

def is_valid_tx_hash(tx_hash: str) -> bool:
    if not isinstance(tx_hash, str):
        return False
    clean_hash = tx_hash[2:] if tx_hash.startswith("0x") else tx_hash
    return bool(re.match(r"^[0-9a-fA-F]{64}$", clean_hash))

def is_valid_private_key(private_key: str) -> bool:
    if not isinstance(private_key, str):
        return False
    clean_key = private_key[2:] if private_key.startswith("0x") else private_key
    return bool(re.match(r"^[0-9a-fA-F]{64}$", clean_key))