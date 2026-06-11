import pandas as pd

# 1. READ (The 'E' in ETL)
# Pandas automatically knows what is a header and what is a number
df = pd.read_csv("inventory_data.csv")

print("--- Original Data ---")
print(df)

# 2. TRANSFORM (Applying logic to entire columns at once)
# This is 'Vectorized' thinking—no more manual for loops!
df.loc[df['price'] > 10000, 'price'] = df['price'] * 0.9
df.loc[df['price'] < 2000, 'price'] = df['price'] + 500

print("\n--- Updated Data ---")
print(df)

# 3. LOAD (Save to CSV)
df.to_csv("pandas_inventory.csv", index=False)