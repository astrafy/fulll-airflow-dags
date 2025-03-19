# from airflow.decorators import task, dag
# from airflow.operators.empty import EmptyOperator
# from datetime import datetime
#
# @dag(
#     dag_id="easy_dag_with_decorators",
#     start_date=datetime(2024, 4, 29),
# )
# def my_dag():
#
#     @task
#     def print_hello():
#         print("Hello")
#
#     print_hello >> EmptyOperator(task_id="goodbye")
#
# my_dag()