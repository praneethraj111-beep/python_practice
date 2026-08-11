import logging
from src.tracker_logging import setup_logging
from src.database import init_db
from src.pipeline import run_pipeline

def main():
    # 1. Initialize Logging
    setup_logging()
    
    # 2. Verify Database Schema
    logging.info("Starting Market & Expense Pipeline...")
    init_db()
    
    # 3. Run Pipeline Operations
    run_pipeline()
    
    logging.info("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()