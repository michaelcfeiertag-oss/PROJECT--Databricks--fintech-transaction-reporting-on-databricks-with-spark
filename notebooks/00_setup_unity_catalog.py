# Databricks notebook source
# MAGIC %md
# MAGIC # 00 — Setup Unity Catalog


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Create or confirm the Unity Catalog objects used in this project and copy the sample CSV files into the governed raw data volume.

# COMMAND ----------
catalog_name = "fintech_dev"
schema_name = "reporting"
volume_name = "raw_data"

raw_volume_path = f"/Volumes/{catalog_name}/{schema_name}/{volume_name}"

print("Raw volume path:", raw_volume_path)

# COMMAND ----------
# TODO:
# 1. Run SQL to create the catalog if needed.
# 2. Run SQL to create the schema if needed.
# 3. Run SQL to create the volume if needed.

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {catalog_name}.{schema_name}.{volume_name}")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Copy sample files into the volume
# MAGIC Update the repo path if needed to match your Git folder location.

# COMMAND ----------
repo_sample_path = "file:/Workspace/Repos/your-user/fintech-transaction-reporting-project/sample_data"
dbutils.fs.mkdirs(raw_volume_path)

# TODO:
# Copy the three sample CSV files from the repo folder into the UC volume.
# If the repo path is different in your workspace, update repo_sample_path first.

files_to_copy = ["transactions_sample.csv", "customers_sample.csv", "accounts_sample.csv"]

for file_name in files_to_copy:
    source = f"{repo_sample_path}/{file_name}"
    target_name = file_name.replace("_sample", "")
    target = f"{raw_volume_path}/{target_name}"
    print(f"Copying {source} -> {target}")
    try:
        dbutils.fs.cp(source, target)
    except Exception as e:
        print("Copy skipped or failed:", e)

# COMMAND ----------
display(dbutils.fs.ls(raw_volume_path))

# COMMAND ----------
# MAGIC %md
# MAGIC ## Reflection
# MAGIC Why are raw CSV files stored as volume files, while curated outputs are better stored as Unity Catalog tables?

