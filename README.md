# Fintech Transaction Reporting on Databricks with Spark

A self-learning starter project for Week 6 of the Databricks and Spark phase.

This repo is designed to help students practice:
- structured Spark DataFrame workflows
- layered Spark SQL using temporary views
- practical performance thinking
- Unity Catalog-aware data organization
- professional Databricks project structure with GitHub
- lightweight workflow automation thinking

## Project theme
A fintech operations team needs transaction reporting from raw daily transaction data. Students will read raw CSV files from a Unity Catalog volume, prepare clean transaction data, build staged SQL reporting logic, create final reporting outputs, and reflect on workflow design.

## Student skill baseline
This project assumes students already know how to:
- work in Databricks notebooks
- build Spark DataFrame workflows
- use temporary views
- write layered SQL
- think about readability and debugging
- apply beginner-to-intermediate Spark performance reasoning

This project **builds forward** from that level.

## Recommended repo flow
1. Read this README.
2. Open `PROJECT_ASSIGNMENT.md`.
3. Review `config/uc_names.md`.
4. Run `notebooks/00_setup_unity_catalog.py`.
5. Work through the notebooks in order.
6. Complete all TODO sections.
7. Create the final reporting outputs.
8. Answer the reflection prompts.
9. Review `docs/automation_guide.md`.

## Suggested notebook order
1. `00_setup_unity_catalog.py`
2. `01_project_orientation.py`
3. `02_ingest_raw_from_volume.py`
4. `03_prepare_silver_data.py`
5. `04_build_gold_reports.py`
6. `05_data_quality_checks.py`
7. `06_reflection_and_automation.py`

## Unity Catalog pattern used in this project
This repo teaches the following structure:
- raw files in a Unity Catalog volume
- curated data in Unity Catalog managed tables
- code stored in GitHub
- execution run from Databricks notebooks
- optional automation through a Databricks job

### Naming convention
- Catalog: `fintech_dev`
- Schema: `reporting`
- Volume: `raw_data`

### Example raw file paths
- `/Volumes/fintech_dev/reporting/raw_data/transactions.csv`
- `/Volumes/fintech_dev/reporting/raw_data/customers.csv`
- `/Volumes/fintech_dev/reporting/raw_data/accounts.csv`

### Example target tables
- `fintech_dev.reporting.silver_transactions`
- `fintech_dev.reporting.gold_daily_summary`
- `fintech_dev.reporting.gold_failed_transactions`
- `fintech_dev.reporting.gold_high_value_transfers`
- `fintech_dev.reporting.gold_payment_channel_summary`

## Repo structure
```text
fintech-transaction-reporting-project/
├── README.md
├── PROJECT_ASSIGNMENT.md
├── databricks.yml
├── .gitignore
├── config/
├── notebooks/
├── sql/
├── src/
├── sample_data/
├── docs/
└── .github/
```

## What students should submit
- completed notebooks
- final report tables or screenshots
- brief answers to the reflection prompts
- a short project summary in markdown

## Notes on GitHub and Databricks
GitHub is the source of truth for code, docs, and sample inputs. Live Unity Catalog objects and runtime state are not stored in GitHub. Students should keep the repo organized and commit by logical stage.

## Suggested commit flow
- commit 1: repo setup and orientation
- commit 2: ingestion from Unity Catalog volume
- commit 3: silver preparation logic
- commit 4: gold reporting logic
- commit 5: data quality checks
- commit 6: reflection and cleanup
