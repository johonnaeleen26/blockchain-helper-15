import re

EVM_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
SOLANA_ADDRESS_PATTERN = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")
BTC_ADDRESS_PATTERN = re.compile(
    r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39,59})$"
)


def is_valid_evm_address(address: str) -> bool:
    if not address or not isinstance(address, str):
        return False
    return bool(EVM_ADDRESS_PATTERN.match(address))


def is_valid_solana_address(address: str) -> bool:
    if not address or not isinstance(address, str):
        return False
    return bool(SOLANA_ADDRESS_PATTERN.match(address))


def is_valid_btc_address(address: str) -> bool:
    if not address or not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_PATTERN.match(address))


def validate_blockchain_address(address: str, chain: str) -> bool:
    chain_lower = chain.strip().lower()
    if chain_lower in ("eth", "ethereum", "evm", "bsc", "polygon"):
        return is_valid_evm_address(address)
    if chain_lower in ("sol", "solana"):
        return is_valid_solana_address(address)
    if chain_lower in ("btc", "bitcoin"):
        return is_valid_btc_address(address)
    raise ValueError(f"unsupported blockchain: {chain}")
