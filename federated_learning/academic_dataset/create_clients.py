import pandas as pd

df = pd.read_csv("data/academic_verification.csv")

modules = df["code_module"].unique()

print("Modules found:")
print(modules)

for module in modules:

    client_df = df[
        df["code_module"] == module
    ]

    filename = f"data/client_{module}.csv"

    client_df.to_csv(
        filename,
        index=False
    )

    print(
        f"{module}: {len(client_df)} records"
    )