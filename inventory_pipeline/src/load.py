import sqlite3
import pandas as pd

def load_to_database(df: pd.DataFrame, db_path: str, table_name: str):
    """
    Establishes a connection to SQLite and streams the cleaned DataFrame 
    into a structured database table. Overwrites previous entries.
    """
    print(f"[LOAD] Preparing to stream records to database at: {db_path}")
    try:
        # Establish connection (SQLite auto-creates the file if missing)
        conn = sqlite3.connect(db_path)
        
        # Load the records
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"[LOAD] Success! Database table '{table_name}' populated.")
        
        conn.close()
    except Exception as e:
        raise RuntimeError(f"[ERROR] Database ingestion failed: {e}")