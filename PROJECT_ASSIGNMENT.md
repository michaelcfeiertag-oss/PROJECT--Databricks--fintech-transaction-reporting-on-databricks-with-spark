# Project Assignment

## Title
Fintech Transaction Reporting on Databricks with Spark

## Duration
Designed to cover approximately **6 hours** of self-learning work.

## Project goal
Build a small but structured fintech transaction reporting workflow in Databricks using Spark. The project should reflect both:
1. good Spark workflow design
2. good Databricks project organization

## Business scenario
A fintech operations team receives daily transaction exports and needs reliable reporting on:
- daily transaction activity
- failed transactions
- high-value transfers
- payment channel performance
- international transaction patterns

The team wants the work organized so it can later become a repeatable reporting pipeline.

## Your tasks

### Part 1 — Understand the project structure
- Review the repo structure.
- Review the Unity Catalog naming convention in `config/uc_names.md`.
- Understand where raw files live and where curated outputs should be saved.

### Part 2 — Set up Unity Catalog objects
- Create or confirm the catalog, schema, and volume.
- Copy sample CSV files into the Unity Catalog volume.
- Verify that the files are accessible from the `/Volumes/...` path.

### Part 3 — Load the raw datasets
Read:
- transactions
- customers
- accounts

Inspect:
- schema
- row counts
- key columns
- data types

### Part 4 — Prepare the silver transaction dataset
Use PySpark DataFrame logic to:
- select useful columns
- filter invalid rows
- standardize statuses and channels
- derive reporting fields
- join supporting customer and account fields
- create a clean working dataset

Save the result as:
- `fintech_dev.reporting.silver_transactions`

### Part 5 — Build gold reporting outputs
Create final reporting outputs for:
- daily transaction summary
- failed transaction summary
- high-value transfers
- payment channel summary
- international transaction summary

Save them as Unity Catalog managed tables.

### Part 6 — Data quality checks
Create checks for:
- duplicate transaction IDs
- null values in critical fields
- invalid amounts
- cleaned row count compared with raw row count
- rejected or excluded records

### Part 7 — Reflection and automation
Answer the reflection prompts in the final notebook and define a simple automation approach:
- either create a Databricks job
- or document the intended job flow if the feature is not available

## Deliverables
- completed notebooks
- saved silver and gold tables
- completed reflection responses
- screenshots or table previews for final outputs

## Constraints
- Use Databricks notebooks.
- Use Spark DataFrames and Spark SQL.
- Use Unity Catalog paths and table names provided in the repo.
- Keep the project structure organized.
- Do not collapse all logic into one long notebook.

## Success criteria
A strong submission will:
- use clear staged logic
- show readable DataFrame transformations
- use temporary views meaningfully
- produce correct gold reporting outputs
- apply practical performance thinking
- follow the repo structure cleanly
