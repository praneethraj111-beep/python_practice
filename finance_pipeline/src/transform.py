import pandas as pd
import numpy as np

def transform_financial_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans structural string/numeric anomalies and flags high-risk 
    transactions using dynamic fraud detection logic.
    """
    print("[TRANSFORM] Executing corporate financial validation protocols...")
    
    # 1. Deduplication: Clean explicit duplicate transaction IDs
    df = df.drop_duplicates(subset=['transaction_id']).reset_index(drop=True)
    
    # 2. String Normalization: Strip hidden whitespace padding from text columns
    for col in ['transaction_type', 'status']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.upper()
            
    # 3. Data Integrity: Drop transactions missing critical Account IDs
    df = df.dropna(subset=['account_id'])
    
    # 4. Value Correction: Absolute magnitude force for transaction values
    # Converts negative entries (like our withdrawal anomaly) into absolute values
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df['amount'] = df['amount'].abs()
        
    # 5. FRAUD ENGINE LOGIC: Flag accounts running high operational risks
    # Rule A: Flags any single transfer over $50,000 as "HIGH_VALUE_ALERT"
    # Rule B: Flags any transaction marked as "FAILED" as a operational flag
    df['risk_score'] = 'LOW_RISK'
    
    df.loc[(df['amount'] >= 50000.0) & (df['transaction_type'] == 'TRANSFER'), 'risk_score'] = 'HIGH_VALUE_ALERT'
    df.loc[df['status'] == 'FAILED', 'risk_score'] = 'FAILED_TX_FLAG'
    
    print(f"[TRANSFORM] Normalization complete. Cleaned and risk-assessed records: {len(df)}")
    return df