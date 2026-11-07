from web3 import Web3
import json
import uuid

def create_identity(student_id):

    account = Web3().eth.account.create()

    wallet_address = account.address

    node_id = f"NODE_{student_id}"

    return {
        "nodeId": node_id,
        "walletAddress": wallet_address
    }