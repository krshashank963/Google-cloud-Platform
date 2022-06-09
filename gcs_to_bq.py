from typing import Any
import airflow
from airflow import models
from airflow.operators import bash_operator

from datetime import timedelta, datetime
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator



args = {
    'owner': 'shashank',
    'start_date': datetime(2015, 6, 4)
}

dag = models.DAG(
    dag_id='gcs_to_bq', default_args=args,
    schedule_interval=None)

'''create_test_dataset = bash_operator.BashOperator(
    task_id='create_airflow_test_dataset',
    bash_command='bq mk airflow_test',
    dag=dag)
'''
# [START howto_operator_gcs_to_bq]
load_csv = GoogleCloudStorageToBigQueryOperator(
    task_id='gcs_to_bq_example',
    bucket='shashank_dataflow',
    source_objects=['dags_company_data.csv'],
    destination_project_dataset_table='training-freshers.shashank_de_training.gcs_to_bq',
   
    write_disposition='WRITE_TRUNCATE',
    dag=dag)
load_csv        