import pandas as pd
import os 

def extract_financial_data(file_path: str) -> pd.DataFrame:
    """
    Safely ingests the raw financial csv records.
    Verifies existence before attempting to open teh data stream
    """
    print(f"\n[EXTRACT] Locating transaction records at: {file_path}")

    # Check if the file actually exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[EXTRACT ERROR] Target file missing: {file_path}")
    
    try:
        #Load file into memory
        df = pd.read_csv(file_path)
        print(f"\n[EXTRACT] Ingestion successful. Captured {len(df)} raw data transaction.")
        return df
    except Exception as e:
        raise IOError(f"[EXTRACT ERROR] Stream corrupted while reading CSV: {e}")