# Architecture Overview

## Learning architecture
This project teaches a lightweight governed lakehouse structure.

### Raw layer
CSV input files live in a Unity Catalog volume:
- `/Volumes/fintech_dev/reporting/raw_data/transactions.csv`
- `/Volumes/fintech_dev/reporting/raw_data/customers.csv`
- `/Volumes/fintech_dev/reporting/raw_data/accounts.csv`

### Silver layer
A cleaned and enriched transaction dataset is created and stored as:
- `fintech_dev.reporting.silver_transactions`

### Gold layer
Business-facing reports are stored as:
- `fintech_dev.reporting.gold_daily_summary`
- `fintech_dev.reporting.gold_failed_transactions`
- `fintech_dev.reporting.gold_high_value_transfers`
- `fintech_dev.reporting.gold_payment_channel_summary`
- `fintech_dev.reporting.gold_international_summary`

## Project structure idea
- GitHub stores source code, notebooks, SQL, docs, and sample data.
- Databricks runs the project logic.
- Unity Catalog governs the storage paths and output tables.
- A Databricks job can later automate notebook execution in sequence.
