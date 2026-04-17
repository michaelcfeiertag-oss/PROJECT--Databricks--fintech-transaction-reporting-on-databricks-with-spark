-- Duplicate transaction IDs
SELECT transaction_id, COUNT(*) AS duplicate_count
FROM fintech_dev.reporting.silver_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- Nulls in critical fields
SELECT
    SUM(CASE WHEN transaction_id IS NULL THEN 1 ELSE 0 END) AS null_transaction_id,
    SUM(CASE WHEN account_id IS NULL THEN 1 ELSE 0 END) AS null_account_id,
    SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS null_customer_id,
    SUM(CASE WHEN report_date IS NULL THEN 1 ELSE 0 END) AS null_report_date
FROM fintech_dev.reporting.silver_transactions;

-- Invalid amounts
SELECT COUNT(*) AS invalid_amount_count
FROM fintech_dev.reporting.silver_transactions
WHERE amount <= 0;
