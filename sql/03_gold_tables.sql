CREATE OR REPLACE TABLE fintech_dev.reporting.gold_daily_summary AS
SELECT
    report_date,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_amount,
    SUM(CASE WHEN transaction_status = 'SUCCESSFUL' THEN 1 ELSE 0 END) AS successful_transactions,
    SUM(CASE WHEN transaction_status = 'FAILED' THEN 1 ELSE 0 END) AS failed_transactions,
    ROUND(AVG(amount), 2) AS avg_amount
FROM silver_transactions_view
GROUP BY report_date;

CREATE OR REPLACE TABLE fintech_dev.reporting.gold_failed_transactions AS
SELECT
    report_date,
    transaction_type,
    payment_channel,
    COUNT(*) AS failed_count,
    ROUND(SUM(amount), 2) AS failed_amount
FROM silver_transactions_view
WHERE transaction_status = 'FAILED'
GROUP BY report_date, transaction_type, payment_channel;

CREATE OR REPLACE TABLE fintech_dev.reporting.gold_high_value_transfers AS
SELECT
    report_date,
    account_id,
    customer_id,
    transaction_id,
    amount,
    transaction_type,
    payment_channel,
    merchant_country
FROM silver_transactions_view
WHERE is_high_value = 1;

CREATE OR REPLACE TABLE fintech_dev.reporting.gold_payment_channel_summary AS
SELECT
    report_date,
    payment_channel,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount,
    ROUND(AVG(amount), 2) AS avg_amount
FROM silver_transactions_view
GROUP BY report_date, payment_channel;

CREATE OR REPLACE TABLE fintech_dev.reporting.gold_international_summary AS
SELECT
    report_date,
    merchant_country,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM silver_transactions_view
WHERE is_international = 1
GROUP BY report_date, merchant_country;
