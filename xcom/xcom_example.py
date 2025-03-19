# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.python import PythonOperator
#
# def push_data_to_xcom(**kwargs):
#     """Pushes data to XCom."""
#     msg = "This is some data to be shared via XCom"
#     kwargs['ti'].xcom_push(key='shared_data', value=msg)
#     print("Data pushed to XCom successfully!")
#
# def pull_data_from_xcom(**kwargs):
#     """Pulls data from XCom."""
#     data = kwargs['ti'].xcom_pull(key='shared_data')
#     print(f"Data retrieved from XCom: {data}")
#
# default_args = {
#     'owner': 'airflow',
#     'start_date': datetime(2024, 4, 29),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }
#
# with DAG(
#     dag_id='xcom_example',
#     default_args=default_args,
#     schedule_interval='@once',
#     catchup=False
# ) as dag:
#
#     push_task = PythonOperator(
#         task_id='push_data',
#         python_callable=push_data_to_xcom,
#         dag=dag
#     )
#
#     pull_task = PythonOperator(
#         task_id='pull_data',
#         python_callable=pull_data_from_xcom,
#         dag=dag
#     )
#
#     push_task >> pull_task
