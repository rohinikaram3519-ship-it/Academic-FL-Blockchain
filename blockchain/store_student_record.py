from web3 import Web3
import pandas as pd

# Connect Ganache

w3 = Web3(
    Web3.HTTPProvider(
        "http://127.0.0.1:8545"
    )
)

# Your deployed contract address

contract_address = "0x0Fc5c29480f4E5894dA7e23678c5eB10Ff38E773"

# Load ABI

import json
import os

BASE_DIR = os.path.dirname(__file__)

with open(
    os.path.join(
        BASE_DIR,
        "build",
        "contracts",
        "AcademicVerification.json"
    ),
    "r"
) as f:

    contract_json = json.load(f)

abi = contract_json["abi"]

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

account = w3.eth.accounts[0]

# Read certificate records

df = pd.read_csv(
    "../federated_learning/academic_dataset/data/certificate_records.csv"
)

# Store first student record

row = df.iloc[0]

tx_hash = contract.functions.addRecord(

    int(row["student_id"]),

    str(row["module"]),

    str(row["certificate_status"]),

    str(row["verification_hash"]),

    str(row["attestation_token"])

).transact(

    {
        "from": account
    }

)

receipt = w3.eth.wait_for_transaction_receipt(
    tx_hash
)

print("Stored Successfully")

print(
    tx_hash.hex()
)