import pandas as pd
import matplotlib.pyplot as plt

# 1. Load your cleaned data
df = pd.read_csv("clean_inventory.csv")

# 2. Define the Chart Layout
# plt.bar(X-axis data, Y-axis data, color)
plt.bar(df['name'], df['price'], color='royalblue')

# 3. Add Labels and Context
plt.title("Current Inventory Price Valuation", fontsize=14, fontweight='bold')
plt.xlabel("Product Name", fontsize=12)
plt.ylabel("Price (INR)", fontsize=12)

# 4. Save the chart as an image file on your computer
plt.savefig("inventory_valuation_chart.png", dpi=300, bbox_inches='tight')

print("Chart generated successfully! Check your file sidebar for 'inventory_valuation_chart.png'.")