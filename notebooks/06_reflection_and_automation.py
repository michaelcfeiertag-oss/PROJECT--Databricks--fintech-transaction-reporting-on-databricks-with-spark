# Databricks notebook source
# MAGIC %md
# MAGIC # 06 — Reflection and Automation


# COMMAND ----------
# MAGIC %md
# MAGIC ## Goal
# MAGIC Reflect on workflow structure, business value, and the first level of automation.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Reflection questions
# MAGIC Answer these in markdown cells:
# MAGIC
# MAGIC 1. Why is the project split into multiple notebooks instead of one large notebook?
# MAGIC 2. Where are the heavier steps in the project?
# MAGIC 3. Which transformations are likely to cause wider Spark work or shuffles?
# MAGIC 4. Why is filtering early a useful design choice here?
# MAGIC 5. Why do raw files belong in a volume while curated outputs belong in managed tables?
# MAGIC 6. Which gold report is most useful for the operations team?
# MAGIC 7. If this project grew larger, what would you improve next?

# COMMAND ----------
# MAGIC %md
# MAGIC ## Automation task
# MAGIC Document a lightweight automation plan.
# MAGIC
# MAGIC Required sequence:
# MAGIC 1. 02_ingest_raw_from_volume
# MAGIC 2. 03_prepare_silver_data
# MAGIC 3. 04_build_gold_reports
# MAGIC 4. 05_data_quality_checks
# MAGIC
# MAGIC In a markdown cell:
# MAGIC - explain the dependency order
# MAGIC - explain what output should exist after each task
# MAGIC - note where the run should stop if a task fails

# COMMAND ----------
# Optional:
# If the Jobs feature is available in your workspace, create the job in the UI and include a screenshot or short description here.

