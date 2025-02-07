
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, Airflow!")

default_args = {"start_date": datetime(2024, 2, 7)}

with DAG("hello_airflow", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    task = PythonOperator(
        task_id="say_hello",
        python_callable=print_hello
    )

    task
