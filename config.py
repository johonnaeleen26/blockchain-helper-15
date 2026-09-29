import os
from typing import Dict, Any

class Config:
    """Centralized configuration management for blockchain-helper-15."""

    def __init__(self) -> None:
        self.network: str = os.getenv("BLOCKCHAIN_NETWORK", "mainnet")
        self.timeout: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    def get_provider_url(self) -> str:
        """Return the appropriate RPC provider URL based on network."""
        providers: Dict[str, str] = {
            "mainnet": "https://mainnet.infura.io/v3/",
            "sepolia": "https://sepolia.infura.io/v3/"
        }
        return providers.get(self.network, "http://localhost:8545")

    def to_dict(self) -> Dict[str, Any]:
        """Export current configuration as a dictionary."""
        return {
            "network": self.network,
            "timeout": self.timeout,
            "debug": self.debug
        }