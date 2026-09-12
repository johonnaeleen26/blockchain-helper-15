# blockchain-helper-15

`blockchain-helper-15` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks like contract event monitoring, gas estimation, and secure wallet management for developers building decentralized applications.

## Features

*   **Gas Oracle Integration:** Automatically fetches current network congestion data to calculate optimal gas fees, minimizing transaction failure rates.
*   **Event Streamer:** A robust listener service that polls blockchain nodes for specific smart contract events and pushes data to your local database.
*   **Wallet Utility Suite:** Securely generates mnemonic phrases, manages keystores, and handles batch transaction signing without exposing private keys.
*   **Multi-Chain Support:** Seamlessly switch between Mainnet, Testnets, and Layer-2 solutions like Polygon or Arbitrum via a unified configuration file.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install -r requirements.txt
```

## Basic Usage

To initialize a connection and fetch the current network gas price, use the following snippet:

```python
from blockchain_helper import Client

# Initialize with your RPC provider URL
client = Client(rpc_url="https://mainnet.infura.io/v3/YOUR_API_KEY")

# Fetch current gas price in Gwei
gas_price = client.get_gas_price()
print(f"Current gas price: {gas_price} Gwei")
```

For advanced event monitoring, refer to the `examples/` directory for implementation patterns regarding websocket connections and asynchronous processing.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.