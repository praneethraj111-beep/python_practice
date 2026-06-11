import pandas as pd

# Load the file we created in the last step
df = pd.read_csv("pandas_inventory.csv")

print("---INVENTORY ANALYTICS REPORT---")

# 1. Total Inventory Value (SUM)
total_value = df['price'].sum()
print(f"Total Value of Inventory: {total_value}")

# 2. Average Item Price (AVG)
average_price = df['price'].mean()
print(f"Average Product Price: {average_price}")

# 3. Total Rows/Items (COUNT)
total_items = df['name'].count()
print(f"Total Unique Items: {total_items}")

print("\n--- HIGH-VALUE ITEMS (> 2000)---")
high_value_df = df[df['price'] > 2000]
print(high_value_df)