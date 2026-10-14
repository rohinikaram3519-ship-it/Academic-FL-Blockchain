import pandas as pd
import hashlib
import os

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "certificate_records.csv"
)

df = pd.read_csv(csv_path)

def generate_hash(row):

    data = (
        str(row["student_id"])
        + row["module"]
        + row["certificate_status"]
    )

    return hashlib.sha256(
        data.encode()
    ).hexdigest()

df["verification_hash"] = df.apply(
    generate_hash,
    axis=1
)

df.to_csv(
    csv_path,
    index=False
)

print(
    df.head()
)