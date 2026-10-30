from flask import Flask, request, jsonify
from flask_cors import CORS

from pdf2image import convert_from_bytes
import pytesseract

import PyPDF2
import re

app = Flask(__name__)

CORS(app)


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
    
    print(
    "NUMBERS FOUND:",
    numbers
)

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


if __name__ == "__main__":

    app.run(
        port=5000,
        debug=True
    )