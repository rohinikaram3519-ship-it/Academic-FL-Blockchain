import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(
    "data/academic_verification.csv"
)

features = [
    "highest_education",
    "age_band",
    "num_of_prev_attempts",
    "studied_credits",
    "disability"
]

target = "certificate_eligible"

for col in [
    "highest_education",
    "age_band",
    "disability",
]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

target_encoder = LabelEncoder()

df[target] = target_encoder.fit_transform(
    df[target]
)

print(df[features + [target]].head())

df.to_csv(
    "data/oulad_processed.csv",
    index=False
)

print("Saved oulad_processed.csv")