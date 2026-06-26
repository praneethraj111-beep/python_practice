import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_stock_report(df: pd.DataFrame, output_image_path: str):
    """
    Analyzes the clean data and auto-generates a stock level visualization.
    """
    print(f"[ANALYTICS] Generating automated stock visualization...")
    
    if 'product_name' not in df.columns or 'quantity' not in df.columns:
        print("[WARNING] Missing required columns for analytics visualization.")
        return

    plt.clf()
    plt.figure(figsize=(8, 5))
    plt.bar(df['product_name'], df['quantity'], color='skyblue', edgecolor='navy')
    
    plt.title('Current Inventory Stock Levels', fontsize=14, fontweight='bold')
    plt.xlabel('Product Name', fontsize=12)
    plt.ylabel('Quantity in Stock', fontsize=12)
    plt.xticks(rotation=15)
    plt.tight_layout()
    
    plt.savefig(output_image_path, dpi=100)
    print(f"[ANALYTICS] Success! Report visualization saved at: {output_image_path}")