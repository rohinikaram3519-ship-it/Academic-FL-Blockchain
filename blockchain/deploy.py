from web3 import Web3
from solcx import compile_source

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print("Connected:", w3.is_connected())

# Load contract
with open("contracts/ModelRegistry.sol", "r") as f:
    source = f.read()

compiled_sol = compile_source(
    source,
    output_values=["abi", "bin"],
    solc_version="0.8.20"
)

contract_id, contract_interface = compiled_sol.popitem()

abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

# Ganache account
account = w3.eth.accounts[0]

# Deploy
ModelRegistry = w3.eth.contract(
    abi=abi,
    bytecode=bytecode
)

tx_hash = ModelRegistry.constructor().transact(
    {
        "from": account
    }
)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract Address:")
print(tx_receipt.contractAddress)