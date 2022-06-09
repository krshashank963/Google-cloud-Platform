from datetime import timedelta, datetime

from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
default_args = {
    'owner': 'Shashank',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 4),
    
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    
}

#define task

with DAG(
    'GCS_to_BQtable',
    default_args=default_args,
    description='Data transfer to a new BQ table',
    schedule_interval=None,
    ) as my_dag:
    

    t1 = GoogleCloudStorageToBigQueryOperator(task_id = "GCS_to_BQ",
        bucket = "shashank_dataflow", 
        source_objects = ['shashank_dataflow/dags_company_data.csv'],
        
        autodetect = True,
        skip_leading_rows = 1,
        create_disposition = "CREATE_IF_NEEDED",
        destination_project_dataset_table = "training-freshers.shashank_de_training.emp2")
        
   

    '''t1 =GoogleCloudStorageToBigQueryOperator(
        task_id='gcs_to_bq_example',
        bucket='cloud-samples-data',
        source_objects=['shashank_dataflow/dags_company_data.csv'],
        destination_project_dataset_table='training-freshers.shashank_de_training',
        schema_fields=[
            {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'post', 'type': 'STRING', 'mode': 'NULLABLE'},
        ],
        write_disposition='WRITE_TRUNCATE',
    )'''
    t1
