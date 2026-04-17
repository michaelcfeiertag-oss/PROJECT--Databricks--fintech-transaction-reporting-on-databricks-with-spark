# Databricks notebook source
# MAGIC %md
# MAGIC # 05 — Data Quality Checks


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Test whether the silver dataset is reliable enough for business reporting.

# COMMAND ----------
from pyspark.sql import functions as F

catalog_name = "fintech_dev"
schema_name = "reporting"

silver_df = spark.table(f"{catalog_name}.{schema_name}.silver_transactions")
raw_df = spark.table("raw_transactions")

# COMMAND ----------
# Duplicate transaction IDs
duplicate_df = (
    silver_df.groupBy("transaction_id")
    .count()
    .filter(F.col("count") > 1)
)

# Null checks
null_check_df = silver_df.select(
    F.sum(F.when(F.col("transaction_id").isNull(), 1).otherwise(0)).alias("null_transaction_id"),
    F.sum(F.when(F.col("account_id").isNull(), 1).otherwise(0)).alias("null_account_id"),
    F.sum(F.when(F.col("customer_id").isNull(), 1).otherwise(0)).alias("null_customer_id"),
    F.sum(F.when(F.col("report_date").isNull(), 1).otherwise(0)).alias("null_report_date"),
)

# Invalid amount checks
invalid_amount_df = silver_df.filter(F.col("amount") <= 0)

# Row count comparison
raw_count = raw_df.count()
silver_count = silver_df.count()
excluded_count = raw_count - silver_count

# COMMAND ----------
print("Raw count:", raw_count)
print("Silver count:", silver_count)
print("Excluded count:", excluded_count)

display(duplicate_df)
display(null_check_df)
display(invalid_amount_df)

# COMMAND ----------
# TODO:
# Add at least two more business-relevant quality checks.
# Examples:
# - unknown transaction_status values
# - unknown payment_channel values
# - missing customer segment after the join
# - missing account status after the join

# COMMAND ----------
# MAGIC %md
# MAGIC ## Reflection prompt
# MAGIC Which quality check would matter most to a fintech operations team, and why?

