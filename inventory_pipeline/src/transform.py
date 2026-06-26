import pandas as pd
import numpy as np

def clean_inventory(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms, normalizes, and validates raw inventory data.
    Enforces strict data quality and integrity constraints.
    """
    print("[TRANSFORM] Executing strict data quality cleaning rules...")
    
    # 1. Drop explicit duplicate entries
    df = df.drop_duplicates().reset_index(drop=True)
    
    # 2. Schema Guard: Drop rows with missing critical identifiers (Product Name)
    if 'product_name' in df.columns:
        initial_count = len(df)
        df = df.dropna(subset=['product_name'])
        df = df[df['product_name'].str.strip() != ""]
        dropped_rows = initial_count - len(df)
        if dropped_rows > 0:
            print(f"[TRANSFORM][ALERT] Dropped {dropped_rows} row(s) due to missing product names.")
            
    # 3. Numeric Guard: Force price to numeric and handle invalid/negative values
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        # Business Rule: If price is negative or missing, default it to 0.00
        df['price'] = df['price'].apply(lambda x: x if (pd.notnull(x) and x >= 0) else 0.0)

    # 4. Quantity Guard: Force quantity to integers and handle negatives
    if 'quantity' in df.columns:
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0)
        # Business Rule: Negative quantities are impossible; reset them to zero stock
        df['quantity'] = df['quantity'].apply(lambda x: int(x) if x >= 0 else 0)
    
    print(f"[TRANSFORM] Integrity checks complete. Valid records to load: {len(df)}")
    return df