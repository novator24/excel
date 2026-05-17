from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def ingest_provider(provider_name: str) -> None:
    # In production this function writes raw payloads to object storage.
    print(f"Ingesting provider: {provider_name}")


with DAG(
    dag_id="provider_ingestion",
    schedule="0 */6 * * *",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["fertifreight", "ingestion"],
) as dag:
    for provider in ("ais", "weather", "port", "sanctions", "fuel", "fx"):
        PythonOperator(
            task_id=f"ingest_{provider}",
            python_callable=ingest_provider,
            op_kwargs={"provider_name": provider},
        )
