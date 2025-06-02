from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from random import randint

@dag(
    dag_id="my_dag_decorator",
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
    default_args={
        'owner': 'airflow',
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    }
)
def my_workflow():

    @task
    def training_model():
        return randint(1, 10)

    @task.branch
    def choose_best_model(acc1, acc2, acc3):
        best = max(acc1, acc2, acc3)
        return "accurate" if best > 8 else "inaccurate"

    acc1 = training_model()
    acc2 = training_model()
    acc3 = training_model()

    decision = choose_best_model(acc1, acc2, acc3)

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate'"
    )

    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
    )

    decision >> [accurate, inaccurate]

my_dag = my_workflow()