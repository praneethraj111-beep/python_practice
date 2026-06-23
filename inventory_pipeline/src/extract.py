import pandas as pd
import os

def extract_raw_data(file_path: str) -> pd.DataFrame:
    """
    Safely reads a CSV file from the raw data directory.
    Includes explicit error handling to ensure the script doesn't crash silently.
    """
    print(f"[EXTRACT] Searching for data at: {file_path}")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] Target data file missing at: {file_path}")
        
    try:
        df = pd.read_csv(file_path)
        print(f"[EXTRACT] Ingestion successful. Loaded {len(df)} records.")
        return df
    except Exception as e:
        raise IOError(f"[ERROR] Failed to parse the CSV data: {e}")