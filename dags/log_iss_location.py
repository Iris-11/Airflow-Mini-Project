from airflow import DAG
from datetime import datetime,timedelta
from airflow.providers.oracle.operators.oracle import OracleOperator
import requests
import oracledb

default_args={
        'owner': 'airflow',
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    }
with DAG(
    dag_id="iss_log_dag",
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(minutes=10),
    catchup=False,
    default_args = default_args
) as dag:
    copy_new_data = OracleOperator(
        task_id='copy_data_to_target',
        oracle_conn_id='oracle_conn',
        sql='BEGIN copy_new_data; END;',
    )