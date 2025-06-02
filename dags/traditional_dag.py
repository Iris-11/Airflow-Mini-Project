from airflow import DAG 
#DAG always required
from datetime import datetime, timedelta
#to set start date
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from random import randint


#creating DAG instace: DAG object with context manager
#parameters- ID, startdate, 
#schedule_interval defines frequency(every 10 mins, daily), 
#using CRON equations or presets like @daily

#dag runs-instances of dag- by default airflow will try to run all the non-triggered dag runs 
#from start date to current date- to avoid this use - catch up = False - only latest one will be run

#note- airflow schedules the first dag at startdate+schedule_interval

#sharing data- xcomm- cross communication message - between tasks in dag for that we need ti(task instance) object-

def _training_model():
    return randint(1,10)

def _choose_best_model(ti):
    #pull accuracies from airflow db using xcomm
    accuracies= ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
    ])
    best_accuracy = max(accuracies)
    if (best_accuracy>8):
        return 'accurate' #return task id for branch operator
    return 'inaccurate'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': timedelta(days=1) 
}

with DAG("my_dag",start_date=datetime(2025,1,1),
        default_args=default_args, catchup=False) as dag:

        #import operator first or nowadays use the decorator

        # create task: needs- id, python function
        training_model_A = PythonOperator(
            task_id="training_model_A",
            python_callable=_training_model
        )

        training_model_B = PythonOperator(
            task_id="training_model_B",
            python_callable=_training_model
        )

        training_model_C = PythonOperator(
            task_id="training_model_C",
            python_callable=_training_model
        )

        choose_best_model = BranchPythonOperator(
            task_id="choose_best_model",
            python_callable=_choose_best_model
        )

        accurate = BashOperator(
            task_id="accurate",
            bash_command="echo 'accurate'"
        )

        inaccurate = BashOperator(
            task_id="inaccurate",
            bash_command="echo 'inaccurate'"
        )

        [training_model_A,training_model_B,training_model_C] >> choose_best_model >> [accurate,inaccurate]