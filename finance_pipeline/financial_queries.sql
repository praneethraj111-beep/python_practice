-- ==========================================================
-- FINANCIAL RISK & AUDIT OPERATIONS LEDGER
-- ==========================================================

-- Query 1: Isolate Critical Threats for Security Operations
-- Instantly extracts high-risk anomalies or failed sequences for human review
SELECT 
    transaction_id,
    account_id,
    amount,
    transaction_type,
    risk_score
FROM secure_transactions
WHERE risk_score IN ('HIGH_VALUE_ALERT', 'FAILED_TX_FLAG')
ORDER BY amount DESC;

---

-- Query 2: Account Exposure Analysis
-- Computes total capital moved and average transaction sizing grouped per account
SELECT 
    account_id,
    COUNT(transaction_id) AS total_transactions_executed,
    SUM(amount) AS total_capital_moved,
    ROUND(AVG(amount), 2) AS average_transaction_magnitude
FROM secure_transactions
GROUP BY account_id
ORDER BY total_capital_moved DESC;

---

-- Query 3: High-Level Corporate Liquidity Summary
-- Aggregates macro-level operational volume metrics across the database
SELECT 
    transaction_type,
    COUNT(*) AS volume_count,
    SUM(amount) AS total_type_volume,
    ROUND(AVG(amount), 2) AS average_type_volume
FROM secure_transactions
GROUP BY transaction_type;