CREATE OR REPLACE TABLE fintech_dev.reporting.silver_transactions AS
SELECT
    transaction_id,
    account_id,
    customer_id,
    transaction_type,
    amount,
    currency,
    transaction_status,
    payment_channel,
    merchant_country,
    report_date,
    amount_band,
    is_high_value,
    is_international,
    customer_segment,
    risk_flag,
    account_type,
    account_status
FROM silver_transactions_view;
