import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class NodeConfig:
    rpc_url: str = "https://cloudflare-eth.com"
    chain_id: int = 1
    timeout: int = 30
    max_retries: int = 3


@dataclass
class AppConfig:
    node: NodeConfig = field(default_factory=NodeConfig)
    gas_limit_multiplier: float = 1.1
    default_account: Optional[str] = None


class ConfigLoader:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path

    def load(self) -> AppConfig:
        data: Dict[str, Any] = {}
        if self.config_path and os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        node_data = data.get("node", {})
        env_rpc = os.getenv("BLOCKCHAIN_RPC_URL")
        if env_rpc:
            node_data["rpc_url"] = env_rpc

        env_chain = os.getenv("BLOCKCHAIN_CHAIN_ID")
        if env_chain and env_chain.isdigit():
            node_data["chain_id"] = int(env_chain)

        node_config = NodeConfig(
            rpc_url=node_data.get("rpc_url", NodeConfig.rpc_url),
            chain_id=node_data.get("chain_id", NodeConfig.chain_id),
            timeout=node_data.get("timeout", NodeConfig.timeout),
            max_retries=node_data.get("max_retries", NodeConfig.max_retries),
        )

        return AppConfig(
            node=node_config,
            gas_limit_multiplier=data.get(
                "gas_limit_multiplier", AppConfig.gas_limit_multiplier
            ),
            default_account=data.get(
                "default_account", os.getenv("DEFAULT_ACCOUNT")
            ),
        )
