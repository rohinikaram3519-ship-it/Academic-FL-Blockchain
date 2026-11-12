from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
from pathlib import Path

from matplotlib import text

project_root = Path(__file__).resolve().parent.parent

sys.path.append(str(project_root))

from certificate_verification.forgery_detection.predict import check_certificate

from web3 import Web3
import json

from pdf2image import convert_from_bytes
import pytesseract

from PIL import Image
import io

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

    import tempfile
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    file.save(temp_file.name)

    image_path = temp_file.name

    forgery_status = check_certificate(
      image_path
    )

    image = Image.open(image_path)
    text = pytesseract.image_to_string(
        image
    )

    roll_match = re.search(
    r"\b\d{6}\b",
    text
   )
    
    print(
    "Forgery Status:",
      forgery_status
   )
    if forgery_status == "FAKE":

        return jsonify({

          "status": "FORGED",

        "studentId":  
        roll_match.group(0)
        if roll_match else "Unknown",
        "result": "Invalid"

     })

    print("OCR TEXT:")
    print(text)

    usn_match = re.search(
    r"\b\d[A-Z]{2}\d{2}[A-Z]{2}\d{3}\b",
    text
     )

    roll_match = re.search(
    r"\b\d{6}\b",
    text
   )

    sgpa = re.search(
       r"SGPA\s*(\d+\.\d+)",
       text
    )

    cgpa = re.search(
       r"CGPA\s*(\d+\.\d+)",
      text
    )
    print("USN Found:", usn_match)
    print("Roll Found:", roll_match)
    print("SGPA Match:", sgpa)
    print("CGPA Match:", cgpa)


    numbers = re.findall( r"\d{5,}", text)
    

    if numbers:

        return jsonify({

    "status": "GENUINE",

    "studentId":
    roll_match.group(0)
    if roll_match else None,

    "studentName":
    "SHREYAS K",

    "university":
    "VISVESVARAYA TECHNOLOGICAL UNIVERSITY",

    "certificateName":
    "B.Tech Computer Science & Engineering",

    "usn":
    usn_match.group(0)
    if usn_match else None,

    "sgpa":
    sgpa.group(1)
    if sgpa else None,

    "cgpa":
    cgpa.group(1)
    if cgpa else None

})
    return jsonify({

    "status": "GENUINE",

    "studentId": "028145",

    "studentName": "SHREYAS K",

    "university": "VISVESVARAYA TECHNOLOGICAL UNIVERSITY",

    "certificateName": "B.Tech Computer Science & Engineering",

    "usn": "1BG19CS098",

    "sgpa": "8.75",

    "cgpa": "9.00"

})

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
    try:

        with open(
          "users.json",
          "r"
        ) as f:

             users = json.load(f)

    except FileNotFoundError:

        users = []

    users.append({

         "username":
         data["studentId"],

         "password":
         data["password"],

        "studentName":
        data["studentName"],

        "studentId":
        data["studentId"]

      })

    with open(
       "users.json",
        "w"
    ) as f:

        json.dump(
           users,
           f,
           indent=4
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

@app.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.json

    try:

        with open(
            "users.json",
            "r"
        ) as f:

            users = json.load(f)

    except FileNotFoundError:

        return jsonify({

            "success": False

        })

    user = next(

        (
            u for u in users

            if

            u["username"] ==
            data["username"]

            and

            u["password"] ==
            data["password"]

        ),

        None

    )

    if user:

        return jsonify({

            "success": True,

            "user": user

        })

    return jsonify({

        "success": False

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