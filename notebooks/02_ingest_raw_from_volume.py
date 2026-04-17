# Databricks notebook source
# MAGIC %md
# MAGIC # 02 — Ingest Raw Data from the Unity Catalog Volume


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Load the raw CSV files from the Unity Catalog volume and perform light inspection before transformation.

# COMMAND ----------
from pyspark.sql import functions as F

catalog_name = "fintech_dev"
schema_name = "reporting"
volume_name = "raw_data"

transactions_path = f"/Volumes/{catalog_name}/{schema_name}/{volume_name}/transactions.csv"
customers_path = f"/Volumes/{catalog_name}/{schema_name}/{volume_name}/customers.csv"
accounts_path = f"/Volumes/{catalog_name}/{schema_name}/{volume_name}/accounts.csv"

# COMMAND ----------
transactions_df = spark.read.option("header", True).option("inferSchema", True).csv(transactions_path)
customers_df = spark.read.option("header", True).option("inferSchema", True).csv(customers_path)
accounts_df = spark.read.option("header", True).option("inferSchema", True).csv(accounts_path)

# COMMAND ----------
# Light inspection
display(transactions_df.groupBy("transaction_status").count().orderBy(F.desc("count")))
display(transactions_df.groupBy("payment_channel").count().orderBy(F.desc("count")))
display(transactions_df.groupBy("transaction_type").count().orderBy(F.desc("count")))

# COMMAND ----------
# TODO:
# Create three raw temporary views:
# - raw_transactions
# - raw_customers
# - raw_accounts

transactions_df.createOrReplaceTempView("raw_transactions")
customers_df.createOrReplaceTempView("raw_customers")
accounts_df.createOrReplaceTempView("raw_accounts")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Student prompt
# MAGIC Before moving forward, identify:
# MAGIC - any columns that may need standardization
# MAGIC - any columns that may contain invalid values
# MAGIC - any join keys you expect to use in the silver stage

