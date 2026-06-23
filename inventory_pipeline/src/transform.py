import pandas as pd

def clean_inventory(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms and standardizes raw inventory data.
    """
    print("[TRANSFORM] Executing cleaning rules...")
    
    # 1. Eliminate explicit duplicates
    df = df.drop_duplicates().reset_index(drop=True)
    
    # 2. Force numeric validation on price column
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['price'] = df['price'].fillna(0.0)
    
    print(f"[TRANSFORM] Cleaning complete. Cleaned record count: {len(df)}")
    return df