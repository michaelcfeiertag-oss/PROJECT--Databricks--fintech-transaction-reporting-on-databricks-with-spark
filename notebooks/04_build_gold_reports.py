# Databricks notebook source
# MAGIC %md
# MAGIC # 04 — Build Gold Reporting Outputs


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Use layered SQL to create business-facing reporting outputs from the silver dataset.

# COMMAND ----------
catalog_name = "fintech_dev"
schema_name = "reporting"

silver_table = f"{catalog_name}.{schema_name}.silver_transactions"

spark.table(silver_table).createOrReplaceTempView("silver_transactions_view")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Stage 1: focused reporting view
# MAGIC Narrow the silver dataset to the fields used often in reporting.

# COMMAND ----------
spark.sql("""
CREATE OR REPLACE TEMP VIEW focused_transactions AS
SELECT
    transaction_id,
    account_id,
    customer_id,
    report_date,
    transaction_type,
    amount,
    transaction_status,
    payment_channel,
    merchant_country,
    amount_band,
    is_high_value,
    is_international
FROM silver_transactions_view
""")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Stage 2: summary views
# MAGIC Create layered summary views instead of one large query.

# COMMAND ----------
spark.sql("""
CREATE OR REPLACE TEMP VIEW daily_summary_view AS
SELECT
    report_date,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_amount,
    SUM(CASE WHEN transaction_status = 'SUCCESSFUL' THEN 1 ELSE 0 END) AS successful_transactions,
    SUM(CASE WHEN transaction_status = 'FAILED' THEN 1 ELSE 0 END) AS failed_transactions,
    ROUND(AVG(amount), 2) AS avg_amount
FROM focused_transactions
GROUP BY report_date
""")

spark.sql("""
CREATE OR REPLACE TEMP VIEW failed_summary_view AS
SELECT
    report_date,
    transaction_type,
    payment_channel,
    COUNT(*) AS failed_count,
    ROUND(SUM(amount), 2) AS failed_amount
FROM focused_transactions
WHERE transaction_status = 'FAILED'
GROUP BY report_date, transaction_type, payment_channel
""")

spark.sql("""
CREATE OR REPLACE TEMP VIEW payment_channel_summary_view AS
SELECT
    report_date,
    payment_channel,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount,
    ROUND(AVG(amount), 2) AS avg_amount
FROM focused_transactions
GROUP BY report_date, payment_channel
""")

# COMMAND ----------
# TODO:
# Create two more temp views:
# 1. high_value_transfers_view
# 2. international_summary_view

spark.sql("""
CREATE OR REPLACE TEMP VIEW high_value_transfers_view AS
SELECT
    report_date,
    account_id,
    customer_id,
    transaction_id,
    amount,
    transaction_type,
    payment_channel,
    merchant_country
FROM focused_transactions
WHERE is_high_value = 1
""")

spark.sql("""
CREATE OR REPLACE TEMP VIEW international_summary_view AS
SELECT
    report_date,
    merchant_country,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM focused_transactions
WHERE is_international = 1
GROUP BY report_date, merchant_country
""")

# COMMAND ----------
# Save the final gold tables
spark.sql(f"CREATE OR REPLACE TABLE {catalog_name}.{schema_name}.gold_daily_summary AS SELECT * FROM daily_summary_view")
spark.sql(f"CREATE OR REPLACE TABLE {catalog_name}.{schema_name}.gold_failed_transactions AS SELECT * FROM failed_summary_view")
spark.sql(f"CREATE OR REPLACE TABLE {catalog_name}.{schema_name}.gold_high_value_transfers AS SELECT * FROM high_value_transfers_view")
spark.sql(f"CREATE OR REPLACE TABLE {catalog_name}.{schema_name}.gold_payment_channel_summary AS SELECT * FROM payment_channel_summary_view")
spark.sql(f"CREATE OR REPLACE TABLE {catalog_name}.{schema_name}.gold_international_summary AS SELECT * FROM international_summary_view")

# COMMAND ----------
display(spark.table(f"{catalog_name}.{schema_name}.gold_daily_summary"))
display(spark.table(f"{catalog_name}.{schema_name}.gold_failed_transactions"))
display(spark.table(f"{catalog_name}.{schema_name}.gold_high_value_transfers"))
display(spark.table(f"{catalog_name}.{schema_name}.gold_payment_channel_summary"))
display(spark.table(f"{catalog_name}.{schema_name}.gold_international_summary"))

