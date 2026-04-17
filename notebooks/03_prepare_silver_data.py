# Databricks notebook source
# MAGIC %md
# MAGIC # 03 — Prepare the Silver Dataset


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Build a clean and enriched transaction dataset using DataFrame logic, then save it as a Unity Catalog managed table.

# COMMAND ----------
from pyspark.sql import functions as F

catalog_name = "fintech_dev"
schema_name = "reporting"

silver_table = f"{catalog_name}.{schema_name}.silver_transactions"

# COMMAND ----------
transactions_df = spark.table("raw_transactions")
customers_df = spark.table("raw_customers")
accounts_df = spark.table("raw_accounts")

# COMMAND ----------
# TODO:
# Build a prepared transaction DataFrame.
# Suggested steps:
# 1. Select the needed columns.
# 2. Filter invalid rows.
# 3. Standardize status and channel values.
# 4. Create report_date.
# 5. Create amount_band.
# 6. Create is_high_value.
# 7. Join customer and account reference data.
# 8. Create is_international by comparing merchant_country and home_country.

prepared_df = (
    transactions_df
    .select(
        "transaction_id",
        "account_id",
        "customer_id",
        "transaction_type",
        "amount",
        "currency",
        "transaction_status",
        "payment_channel",
        "merchant_country",
        "transaction_date"
    )
    .filter(F.col("transaction_id").isNotNull())
    .filter(F.col("account_id").isNotNull())
    .filter(F.col("customer_id").isNotNull())
    .filter(F.col("transaction_date").isNotNull())
    .filter(F.col("amount") > 0)
    .withColumn("transaction_status", F.upper(F.trim(F.col("transaction_status"))))
    .withColumn("payment_channel", F.upper(F.trim(F.col("payment_channel"))))
    .withColumn("transaction_type", F.upper(F.trim(F.col("transaction_type"))))
    .withColumn("merchant_country", F.upper(F.trim(F.col("merchant_country"))))
    .withColumn("report_date", F.to_date("transaction_date"))
    .withColumn(
        "amount_band",
        F.when(F.col("amount") < 100, "LOW")
         .when(F.col("amount") < 1000, "MEDIUM")
         .otherwise("HIGH")
    )
    .withColumn("is_high_value", F.when(F.col("amount") >= 1000, 1).otherwise(0))
    .join(
        customers_df.select("customer_id", "customer_segment", "customer_country", "risk_flag"),
        on="customer_id",
        how="left"
    )
    .join(
        accounts_df.select("account_id", "account_type", "account_status", "home_country"),
        on="account_id",
        how="left"
    )
    .withColumn(
        "is_international",
        F.when(F.col("merchant_country") != F.upper(F.trim(F.col("home_country"))), 1).otherwise(0)
    )
)

# COMMAND ----------
display(prepared_df.limit(20))

# COMMAND ----------
prepared_df.createOrReplaceTempView("silver_transactions_view")

# COMMAND ----------
# TODO:
# Save the silver dataset as a managed Unity Catalog table.
prepared_df.write.mode("overwrite").saveAsTable(silver_table)

# COMMAND ----------
# Optional performance thinking:
# Where are the wider transformations in this notebook?
# Which steps are likely to trigger shuffles?

