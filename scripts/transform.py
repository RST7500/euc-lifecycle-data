import pandas as pd

df = pd.read_excel(
    "raw/product-lifecycle.xlsx"
)

print("Columns found:")

for col in df.columns:
    print(col)

print(df.head())
