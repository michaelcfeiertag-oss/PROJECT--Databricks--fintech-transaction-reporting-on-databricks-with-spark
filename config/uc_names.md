# Unity Catalog Names Used in This Project

## Namespace
- Catalog: `fintech_dev`
- Schema: `reporting`
- Volume: `raw_data`

## Raw file paths
- `/Volumes/fintech_dev/reporting/raw_data/transactions.csv`
- `/Volumes/fintech_dev/reporting/raw_data/customers.csv`
- `/Volumes/fintech_dev/reporting/raw_data/accounts.csv`

## Curated tables
### Silver
- `fintech_dev.reporting.silver_transactions`

### Gold
- `fintech_dev.reporting.gold_daily_summary`
- `fintech_dev.reporting.gold_failed_transactions`
- `fintech_dev.reporting.gold_high_value_transfers`
- `fintech_dev.reporting.gold_payment_channel_summary`
- `fintech_dev.reporting.gold_international_summary`

## Design rule
- Use **volume paths** for raw CSV files.
- Use **three-level table names** for curated Unity Catalog tables.
- Keep the naming convention visible and consistent across the notebooks, SQL files, docs, and GitHub repo.
