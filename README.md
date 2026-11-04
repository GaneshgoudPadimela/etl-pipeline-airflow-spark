# ETL Pipeline - Airflow + Spark

A small data pipeline example: extract ecommerce order data, clean and
aggregate it with Python / Spark, and load daily summaries - orchestrated
with an Airflow DAG.

This mirrors the batch pipelines I have built for ecommerce data:
extract -> transform -> validate -> load, with a daily schedule and retries.

## Layout
- `dags/ecommerce_etl_dag.py` - Airflow DAG (daily, with retries)
- `src/extract.py` - read raw orders (CSV sample included in code path)
- `src/transform.py` - clean, de-duplicate, aggregate by product / day
- `src/load.py` - write the daily summary out
- `spark/product_aggregation.py` - Spark version of the aggregation
- `tests/test_transform.py` - unit tests for the transform step

## Run the transform locally
```bash
pip install -r requirements.txt
pytest
python -m src.transform
```

## Roadmap
- [ ] Add data-quality checks (nulls, negative amounts)
- [ ] Write output as Parquet partitioned by date
- [ ] Add a second DAG for product catalog ingestion
