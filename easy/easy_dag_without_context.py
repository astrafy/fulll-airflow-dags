# from airflow import DAG
# from airflow.operators.empty import EmptyOperator
# from datetime import datetime
#
# dag = DAG(dag_id="easy_dag_without_context",start_date=datetime(2024, 4, 29))
#
# task1 = EmptyOperator(task_id="say_hello")
#
# task1 >> EmptyOperator(task_id="goodbye")