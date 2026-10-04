# blockchain-helper-15

A high-performance Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies complex data retrieval and transaction signing for developers building decentralized applications.

## Features

*   **Async Web3 Interface:** Built on `asyncio` to handle multiple blockchain queries concurrently without blocking execution.
*   **Smart Contract Indexer:** Automated parsing of event logs into structured JSON formats for easier database integration.
*   **Gas Estimation Engine:** Real-time fee calculation logic that monitors mempool congestion to optimize transaction costs.
*   **Wallet Security Suite:** Includes robust mnemonic phrase validation and offline transaction signing capabilities to keep private keys secure.

## Installation

Ensure you have Python 3.9+ installed. Install the library via pip:

```bash
pip install blockchain-helper-15
```

For local development and testing, clone the repository:

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install -r requirements.txt
```

## Basic Usage

Quickly connect to a network and fetch the balance of an address:

```python
from blockchain_helper import Client

# Initialize the helper with your RPC endpoint
client = Client(provider_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID")

# Get ETH balance in Ether
balance = client.get_balance("0x71C7656...73")
print(f"Current Balance: {balance} ETH")

# Estimate gas for a standard transfer
gas_price = client.get_recommended_gas()
print(f"Recommended Gas Price: {gas_price} Gwei")
```

## License

![MIT](https://img.shields.io/badge/license-MIT-blue.svg)

Distributed under the MIT License. See `LICENSE` for more information.