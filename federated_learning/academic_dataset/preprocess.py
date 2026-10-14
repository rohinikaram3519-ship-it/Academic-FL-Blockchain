import pandas as pd

df = pd.read_csv("data/studentInfo.csv")

# Certificate eligibility

df["certificate_eligible"] = df["final_result"].apply(
    lambda x: "Eligible"
    if x in ["Pass", "Distinction"]
    else "Not Eligible"
)

print(
    df[
        ["final_result",
         "certificate_eligible"]
    ].head()
)

df.to_csv(
    "data/academic_verification.csv",
    index=False
)

print("\nSaved:")
print("data/academic_verification.csv")