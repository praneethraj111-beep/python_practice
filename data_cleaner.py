import pandas as pd
import numpy as np

# 1. Load the dirty data
df = pd.read_csv("dirty_inventory.csv")

print("---1. Raw Dirty Data---")
print(df)

# 2. Fix Duplicates AND reset the row numbers cleanly
df = df.drop_duplicates().reset_index(drop=True)
print("\n---2. After Removing Duplicates---")
print(df)

# 3. Handle the "UNKNOWN" text in the price column
# errors='coerce' forces non-numbers (like 'UNKNOWN') to become NaN (Null)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 4. Fill in the missing/NaN values with a default number (e.g., 0)
df['price'] = df['price'].fillna(0)

print("\n---3. Cleaned Final Data---")
print(df)

# Save the clean data
df.to_csv("clean_inventory.csv", index=False)