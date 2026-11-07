from web3 import Web3
import json

w3 = Web3(
    Web3.HTTPProvider(
        "http://127.0.0.1:8545"
    )
)

contract_address = "0x4D343fb8DfaAb94bf4a0ee8068fc14d0f61b00ec"

with open(
    "build/contracts/AcademicVerification.json"
) as f:

    contract_json = json.load(f)

abi = contract_json["abi"]

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

record = contract.functions.getRecord(
    0
).call()

print(record)