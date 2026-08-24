import pandas as pd
df = pd.read_excel(
    "raw/product-lifecycle.xlsx"
)
print("Columns found:")
for column in df.columns:
    print(column)
print(df.head())
