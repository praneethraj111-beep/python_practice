import os
from src.extract import extract_raw_data
from src.transform import clean_inventory
from src.load import load_to_database

def run_pipeline():
    print("\n=== STARTING PRODUCTION INVENTORY PIPELINE ===")
    
    # Define File & Database Configurations
    RAW_DATA_PATH = "data/raw/dirty_inventory.csv"
    PROCESSED_DATA_PATH = "data/processed/clean_inventory.csv"
    DB_PATH = "databases/inventory_system.db"
    TABLE_NAME = "inventory"
    
    # Ensure target structural directories exist programmatically
    for path in [PROCESSED_DATA_PATH, DB_PATH]:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            print(f"[SYSTEM] Auto-creating directory: {directory}")
            os.makedirs(directory, exist_ok=True)
            
    # Step 1: Ingest Raw Data
    raw_df = extract_raw_data(RAW_DATA_PATH)
    
    # Step 2: Clean and Normalize Data
    clean_df = clean_inventory(raw_df)
    
    # Step 3: Cache Clean Data to CSV
    clean_df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"[SYSTEM] Clean data cached locally at: {PROCESSED_DATA_PATH}")
    
    # Step 4: Stream Data to Production Database
    load_to_database(clean_df, DB_PATH, TABLE_NAME)
    
    print("=== PIPELINE COMPLETELY EXECUTION SUCCESSFUL ===\n")

if __name__ == "__main__":
    run_pipeline()