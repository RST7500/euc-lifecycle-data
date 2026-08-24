import pandas as pd

df = pd.read_excel("raw/product-lifecycle.xlsx")
print(df.columns.tolist())  # This will show all available columns
