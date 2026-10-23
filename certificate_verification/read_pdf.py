import PyPDF2

import os

BASE_DIR = os.path.dirname(__file__)

pdf_file = os.path.join(
    BASE_DIR,
    "..",
    "certificates",
    "generated",
    "CERT_11391.pdf"
)

with open(pdf_file, "rb") as file:

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

print(text)

import re

match = re.search(
    r"Student ID\s*:\s*(\d+)",
    text
)

if match:

    student_id = match.group(1)

    print(
        "Extracted Student ID:",
        student_id
    )