from flask import Flask, request, jsonify
from flask_cors import CORS

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

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text

    match = re.search(
        r"Student ID\s*:\s*(\d+)",
        text
    )

    if match:

        return jsonify(
            {
                "studentId":
                match.group(1)
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