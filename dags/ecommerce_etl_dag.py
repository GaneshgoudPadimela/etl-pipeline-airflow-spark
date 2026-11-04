from datetime import datetime, timedelta
try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:
    DAG = None
# DAG definition is illustrative when Airflow is not installed locally.
# In Airflow, this runs extract -> transform -> load daily.
default_args = {"owner": "ganesh", "retries": 2, "retry_delay": timedelta(minutes=5)}
# See src/ for the actual pipeline functions wired into this DAG.
