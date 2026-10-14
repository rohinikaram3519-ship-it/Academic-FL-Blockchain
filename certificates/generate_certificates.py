import pandas as pd
from reportlab.pdfgen import canvas
import os

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "federated_learning",
    "academic_dataset",
    "data",
    "certificate_records.csv"
)

df = pd.read_csv(csv_path)

output_dir = os.path.join(
    BASE_DIR,
    "generated"
)

os.makedirs(
    output_dir,
    exist_ok=True
)

for _, row in df.head(10).iterrows():

    student_id = row["student_id"]

    pdf_file = os.path.join(
    output_dir,
    f"CERT_{student_id}.pdf"
)

    c = canvas.Canvas(pdf_file)

    c.setFont("Helvetica-Bold", 18)

    c.drawString(
        120,
        800,
        "Academic Certificate"
    )

    c.setFont(
        "Helvetica",
        12
    )

    c.drawString(
        100,
        740,
        f"Student ID: {student_id}"
    )

    c.drawString(
        100,
        710,
        f"Module: {row['module']}"
    )

    c.drawString(
        100,
        680,
        f"Status: {row['certificate_status']}"
    )

    c.drawString(
        100,
        650,
        "University: Open University"
    )

    c.save()

print(
    "Certificates Created"
)