import sqlite3
import pandas as pd

def load_financial_data(df: pd.DataFrame, db_path: str, table_name: str):
    """
    Streams the risk-graded DataFrame straight into a local SQLite database.
    Replaces previous tables to ensure a fresh, synchronized analytical ledger.
    """
    print(f"[LOAD] Opening stream to financial database warehouse: {db_path}")
    
    try:
        # Establish connection (Auto-creates the .db file if it doesn't exist)
        conn = sqlite3.connect(db_path)
        
        # Load the records directly to SQL
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"[LOAD] Success! Database table '{table_name}' securely populated.")
        
        conn.close()
    except Exception as e:
        raise RuntimeError(f"[LOAD ERROR] Financial ingestion sequence failed: {e}")