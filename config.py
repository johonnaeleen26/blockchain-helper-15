import os
from typing import Any, Dict


class Config:
    DEFAULT_CONFIG = {
        "RPC_URL": "https://cloudflare-eth.com",
        "CHAIN_ID": 1,
        "TIMEOUT": 30,
        "RETRY_COUNT": 3,
        "GAS_LIMIT_MULTIPLIER": 1.1,
    }

    def __init__(self, custom_config: Dict[str, Any] = None) -> None:
        self._config = self.DEFAULT_CONFIG.copy()
        if custom_config:
            self._config.update(custom_config)
        self._load_from_env()

    def _load_from_env(self) -> None:
        for key, default_val in self.DEFAULT_CONFIG.items():
            env_val = os.getenv(f"BLOCKCHAIN_{key}")
            if env_val is not None:
                target_type = type(default_val)
                try:
                    if target_type is bool:
                        self._config[key] = env_val.lower() in ("true", "1", "yes")
                    else:
                        self._config[key] = target_type(env_val)
                except ValueError:
                    pass

    def get(self, key: str) -> Any:
        return self._config.get(key)

    @property
    def rpc_url(self) -> str:
        return str(self.get("RPC_URL"))

    @property
    def chain_id(self) -> int:
        return int(self.get("CHAIN_ID"))

    @property
    def timeout(self) -> int:
        return int(self.get("TIMEOUT"))

    @property
    def retry_count(self) -> int:
        return int(self.get("RETRY_COUNT"))

    @property
    def gas_limit_multiplier(self) -> float:
        return float(self.get("GAS_LIMIT_MULTIPLIER"))
