from flask import Flask, request, jsonify
from flask_cors import CORS

from web3 import Web3
import json

from pdf2image import convert_from_bytes
import pytesseract

import PyPDF2
import re
app = Flask(__name__)

CORS(app)
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(
    Web3.HTTPProvider(ganache_url)
)

with open(
    "../blockchain/build/contracts/StudentRegistry.json"
) as f:

    contract_json = json.load(f)

abi = contract_json["abi"]

contract_address = (
    "0x5E20e5210dCC34005A6B41ECcB40678FDfC49431"
)

contract = web3.eth.contract(
    address=contract_address,
    abi=abi
)


@app.route("/")
def home():

    return "Flask Backend Running Successfully"

@app.route("/extract", methods=["POST"])
def extract_student():

    if "file" not in request.files:

        return jsonify(
            {
                "error":
                "No file uploaded"
            }
        )

    file = request.files["file"]

    pages = convert_from_bytes(
        file.read()
  )

    text = ""

    for page in pages:

       text += pytesseract.image_to_string(
          page
    )

    print(text)

    numbers = re.findall( r"\d{5,}", text)
    

    if numbers:

        return jsonify(
            {
                "studentId":
                 numbers[0]
            }
        )

    return jsonify(
        {
            "studentId": None
        }
    )

@app.route(
    "/register",
    methods=["POST"]
)
def register_student():

    data = request.json

    print("REGISTER API CALLED")
    print(data)

    account = Web3().eth.account.create()

    wallet_address = account.address

    node_id = (
        f"NODE_{data['studentId']}"
    )

    print(
        "Student ID:",data['studentId']
    )

    print(
        "Node ID:",
        node_id
    )

    print(
        "Wallet:",
        wallet_address
    )

    tx = contract.functions.registerStudent(

        int(data['studentId']),

        node_id,

        wallet_address

    ).transact({

        "from":
        web3.eth.accounts[0]

    })

    receipt = web3.eth.wait_for_transaction_receipt(tx)

    return jsonify({

        "studentId":
        data["studentId"],

        "studentName":
        data["studentName"],

        "nodeId":
        node_id,

        "walletAddress":
        wallet_address,

        "status":
        "Registered"

    })

@app.route("/test")
def test():

    return jsonify({

        "contract":
        contract.address

    })
    
if __name__ == "__main__":

    app.run(
        port=5000,
        debug=True
    )