import pandas as pd

df = pd.read_csv("data/studentInfo.csv")

print("Columns:")
print(df.columns)

print("\nUnique Final Results:")
print(df["final_result"].unique())