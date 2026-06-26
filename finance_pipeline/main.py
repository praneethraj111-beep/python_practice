import os
from src.extract import extract_financial_data
from src.transform import transform_financial_data
from src.load import load_financial_data
from src.analytics import generate_risk_report

def run_pipeline():
    print("\n=== STARTING AUTOMATED FINANCIAL FRAUD PIPELINE ===")
    
    # Core Path Mapping Configuration
    RAW_DATA_PATH = "data/raw/raw_transactions.csv"
    PROCESSED_DATA_PATH = "data/processed/clean_transactions.csv"
    REPORT_PATH = "data/processed/risk_distribution_report.png"
    DB_PATH = "databases/financial_warehouse.db"
    TABLE_NAME = "secure_transactions"
    
    # Operational Directory Guard
    for path in [PROCESSED_DATA_PATH, REPORT_PATH, DB_PATH]:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
    # Step 1: Extract Ingestion Data Stream
    raw_df = extract_financial_data(RAW_DATA_PATH)
    
    # Step 2: Transform Data Integrity & Flag Risk Profile
    clean_df = transform_financial_data(raw_df)
    
    # Step 3: Cache Structured CSV Ledger
    clean_df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"[SYSTEM] Clean transaction ledger cached at: {PROCESSED_DATA_PATH}")
    
    # Step 4: Stream Into Secure SQL Warehouse
    load_financial_data(clean_df, DB_PATH, TABLE_NAME)
    
    # Step 5: Execute Automated Reporting Analytics
    generate_risk_report(clean_df, REPORT_PATH)
    
    print("=== FINANCIAL PIPELINE EXECUTION SUCCESSFUL ===\n")

if __name__ == "__main__":
    run_pipeline()