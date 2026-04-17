# Databricks notebook source
# MAGIC %md
# MAGIC # 01 — Project Orientation


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Understand the project structure, business context, datasets, and target outputs before building the workflow.

# COMMAND ----------
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
print("Transactions row count:", transactions_df.count())
print("Customers row count:", customers_df.count())
print("Accounts row count:", accounts_df.count())

# COMMAND ----------
transactions_df.printSchema()
customers_df.printSchema()
accounts_df.printSchema()

# COMMAND ----------
display(transactions_df.limit(10))
display(customers_df.limit(10))
display(accounts_df.limit(10))

# COMMAND ----------
# MAGIC %md
# MAGIC ## Student tasks
# MAGIC Answer the following in markdown cells:
# MAGIC 1. Which transaction columns will matter most for reporting?
# MAGIC 2. Which supporting fields from the customer and account datasets may help enrich the reports?
# MAGIC 3. Which final report do you think the fintech operations team will use most often?

