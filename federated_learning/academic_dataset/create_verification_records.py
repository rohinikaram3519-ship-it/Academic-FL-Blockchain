import pandas as pd

df = pd.read_csv(
    "data/academic_verification.csv"
)

verification_df = pd.DataFrame()

verification_df["student_id"] = df["id_student"]

verification_df["module"] = df["code_module"]

verification_df["certificate_status"] = (
    df["certificate_eligible"]
)

verification_df.to_csv(
    "data/certificate_records.csv",
    index=False
)

print(
    verification_df.head()
)

print(
    "\ncertificate_records.csv created"
)