import os
from src.extract import extract_raw_data
from src.transform import clean_inventory
from src.load import load_to_database
from src.analytics import generate_stock_report

def run_pipeline():
    print("\n=== STARTING PRODUCTION INVENTORY PIPELINE ===")
    
    # Configurations
    RAW_DATA_PATH = "data/raw/dirty_inventory.csv"
    PROCESSED_DATA_PATH = "data/processed/clean_inventory.csv"
    REPORT_PATH = "data/processed/stock_levels_report.png"
    DB_PATH = "databases/inventory_system.db"
    TABLE_NAME = "inventory"
    
    # Auto-verify directories exist
    for path in [PROCESSED_DATA_PATH, REPORT_PATH, DB_PATH]:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
    # Step 1: Ingest
    raw_df = extract_raw_data(RAW_DATA_PATH)
    
    # Step 2: Clean
    clean_df = clean_inventory(raw_df)
    
    # Step 3: Cache CSV Backup
    clean_df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"[SYSTEM] Clean data cached locally at: {PROCESSED_DATA_PATH}")
    
    # Step 4: Stream to Database
    load_to_database(clean_df, DB_PATH, TABLE_NAME)
    
    # Step 5: Automated Analytics Reporting
    generate_stock_report(clean_df, REPORT_PATH)
    
    print("=== PIPELINE COMPLETELY EXECUTION SUCCESSFUL ===\n")

if __name__ == "__main__":
    run_pipeline()