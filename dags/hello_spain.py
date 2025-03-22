from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the Python function
def hello_italy():
    print("Hello, italy!")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'hello_italy_dag',
    default_args=default_args,
    description='A simple Hello italy DAG',
    schedule_interval=None,  # Runs only once (manual trigger)
    tags=["customer", "fulll"]
)

# Define the task using the PythonOperator
hello_task = PythonOperator(
    task_id='hello_italy_task',
    python_callable=hello_italy,
    dag=dag,
)

# Set the task order
hello_task
