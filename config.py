import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "chain_id": 1,
    "gas_limit": 21000,
    "max_fee_per_gas_gwei": 50.0,
    "max_priority_fee_gwei": 1.5,
    "request_timeout": 30,
    "retry_attempts": 3,
}


class Config:
    def __init__(self, overrides: Dict[str, Any] | None = None) -> None:
        self._config = DEFAULT_CONFIG.copy()
        if overrides:
            self._config.update(overrides)
        self._load_from_env()

    def _load_from_env(self) -> None:
        env_mappings = {
            "ETH_RPC_URL": ("rpc_url", str),
            "ETH_CHAIN_ID": ("chain_id", int),
            "ETH_GAS_LIMIT": ("gas_limit", int),
            "ETH_MAX_FEE_GWEI": ("max_fee_per_gas_gwei", float),
            "ETH_MAX_PRIORITY_FEE_GWEI": ("max_priority_fee_gwei", float),
            "ETH_TIMEOUT": ("request_timeout", int),
            "ETH_RETRY_ATTEMPTS": ("retry_attempts", int),
        }
        for env_var, (key, cast_type) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    self._config[key] = cast_type(val)
                except ValueError:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()
