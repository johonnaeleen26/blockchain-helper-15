import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://eth.llamarpc.com",
    "chain_id": 1,
    "timeout": 30,
    "gas_multiplier": 1.15,
    "max_retries": 3,
    "use_wss": False,
}


class ConfigLoader:
    def __init__(self, overrides: Optional[Dict[str, Any]] = None):
        self._config = DEFAULT_CONFIG.copy()
        if overrides:
            self._config.update(overrides)
        self._load_from_env()

    def _load_from_env(self) -> None:
        env_mappings = {
            "BLOCKCHAIN_RPC_URL": ("rpc_url", str),
            "BLOCKCHAIN_CHAIN_ID": ("chain_id", int),
            "BLOCKCHAIN_TIMEOUT": ("timeout", int),
            "BLOCKCHAIN_GAS_MULTIPLIER": ("gas_multiplier", float),
            "BLOCKCHAIN_MAX_RETRIES": ("max_retries", int),
        }
        for env_var, (key, type_cast) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    self._config[key] = type_cast(val)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        return self._config.copy()
