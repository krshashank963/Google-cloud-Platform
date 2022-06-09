from airflow.providers.google.cloud.transfers.bigquery_to_gcs import BigQueryToGCSOperator
from typing import Any

import airflow
from airflow import models
from airflow.operators import bash_operator

from datetime import timedelta, datetime

PROJECT_ID = 'training-freshers'
DATASET_NAME = 'shashank_de_training'
DATA_EXPORT_BUCKET_NAME = "shashank_dataflow"
TABLE = 'Sales Records'

with models.DAG(
    "example_bigquery_to_gcs",
    schedule_interval=None,  # Override to match your needs
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
    ) as dag:
    bigquery_to_gcs = BigQueryToGCSOperator(
        task_id="bigquery_to_gcs",
        source_project_dataset_table="shashank_de_training.Sales Records",
        destination_cloud_storage_uris="gs://shashank_dataflow/export-bigquery.csv",
    )
    bigquery_to_gcs