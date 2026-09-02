[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# blockchain-helper-15

blockchain-helper-15 provides a streamlined Python interface for essential blockchain operations in crypto projects. Developers can quickly generate wallets, sign transactions, and fetch on-chain data across EVM networks with minimal boilerplate code.

## Features
- Generate secure BIP-39 compliant wallets with private key derivation
- Build and sign Ethereum transactions with automatic gas and nonce handling
- Retrieve account balances and token holdings from multiple blockchain networks
- Verify signatures and interact with basic smart contract functions

## Installation

```bash
git clone https://github.com/Developer/blockchain-helper-15.git
cd blockchain-helper-15
pip install .
```

## Basic Usage

```python
from blockchain_helper_15 import Wallet

wallet = Wallet.new()
print(wallet.address)

tx_params = {
    "to": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "value": 10**18,
    "chain_id": 1
}
signed_tx = wallet.sign_transaction(tx_params)
```

## License

This project is licensed under the MIT License.