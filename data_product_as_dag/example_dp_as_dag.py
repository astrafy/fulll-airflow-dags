# from airflow.decorators import task
# from airflow.operators.python import get_current_context
# from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
# import sys
# import os
#
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# # Local imports
# from dependencies.runtime_vars import DbtRunDefaults, ConfigVars
# from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
# from airflow import DAG
# from airflow.models import Variable
# from airflow.models.param import Param
# from datetime import datetime, timedelta
# from airflow.utils.task_group import TaskGroup
# from dependencies.runtime_vars import set_env_vars
#
# data_product = "sales_marketing"
# ENV = Variable.get("ENV", default_var="dev")
#
# # Set RunTime Vars
# config_vars = ConfigVars()
# dbt_defaults = DbtRunDefaults(data_product=data_product, environment=ENV)
# airbyte_conn_id = 'f68a6930-4c81-4ed1-bd00-5365180fea55'
#
# config_vars.env_vars.extend([
#     set_env_vars(name="DATA_PRODUCT", value=data_product),
#     set_env_vars(name="ENV", value=ENV)]
# )
#
# DP_SALES_MARKETING_VERSION = Variable.get("DP_SALES_MARKETING_VERSION")
#
# dbt_run_defaults = dict(
#     image_pull_policy=dbt_defaults.image_pull_policy,
#     cmds=dbt_defaults.cmds,
#     namespace=dbt_defaults.namespace,
#     get_logs=dbt_defaults.get_logs,
#     service_account_name=dbt_defaults.service_account_name,
#     affinity=dbt_defaults.affinity,
#     image=f"{dbt_defaults.docker_image}/dbt/{data_product}:{DP_SALES_MARKETING_VERSION}",
#     env_vars=config_vars.env_vars
# )
#
# def construct_dbt_run_command(selector, mode):
#     run_command = f"""
#         dbt run {dbt_defaults.dbt_args} --selector {selector} {mode}; exit $?;
#     """
#     return run_command
#
# run_test = f"""
#     dbt test {dbt_defaults.dbt_args};exit $?;
# """
# edr_report = f"""
#     export DBT_PROFILES_DIR=/app/artifacts
#     edr send-report --gcs-bucket-name dbt_elementary_astrafy_{data_product}_{ENV}
# """
#
# with DAG(
#     dag_id=f'{data_product}-k8s-dag-{ENV}',
#     schedule='0 10 * * *',
#     description='Dag for the Sales Marketing data product',
#     max_active_tasks=10,
#     catchup=False,
#     is_paused_upon_creation=True,
#     tags=['k8s', 'sales_marketing'],
#     max_active_runs=1,
#     dagrun_timeout=timedelta(seconds=36000),
#     default_view='grid',
#     orientation='LR',
#     sla_miss_callback=None,
#     on_success_callback=None,
#     on_failure_callback=None,
#     params={"is_full_refresh": Param(False, type="boolean")},
#     start_date=datetime(2024, 4, 29),
#     default_args={'owner': 'nawfel.bacha', 'retries': 1,
#                   'retry_delay': timedelta(seconds=60)},
#     doc_md=__doc__,
# ) as dag:
#
#     airbyte_sync = AirbyteTriggerSyncOperator(
#         task_id='airbyte_sync',
#         airbyte_conn_id='airbyte_default',
#         connection_id=airbyte_conn_id,
#         asynchronous=False,
#         timeout=3600,
#         wait_seconds=3, dag=dag
#     )
#
#     with TaskGroup(group_id="Transformations") as Transformations:
#         dbt_run_stg = KubernetesPodOperator(
#             **dbt_run_defaults,
#             task_id='dbt_run_stg',
#             name='dbt_run_stg',
#             arguments=[" {{ti.xcom_pull(task_ids='get_dbt_mode_parameter', key='return_value')[0] }}"],
#         )
#
#         dbt_run_dw = KubernetesPodOperator(
#             **dbt_run_defaults,
#             task_id='dbt_run_dw',
#             name='dbt_run_dw',
#             arguments=[" {{ti.xcom_pull(task_ids='get_dbt_mode_parameter', key='return_value')[1] }}"],
#         )
#
#         dbt_run_dm = KubernetesPodOperator(
#             **dbt_run_defaults,
#             task_id='dbt_run_dm',
#             name='dbt_run_dm',
#             arguments=[" {{ti.xcom_pull(task_ids='get_dbt_mode_parameter', key='return_value')[2] }}"],
#         )
#
#         dbt_run_test = KubernetesPodOperator(
#             **dbt_run_defaults,
#             task_id='dbt_run_test',
#             name='dbt_run_test',
#             arguments=[run_test],
#         )
#
#     edr_report = KubernetesPodOperator(
#         **dbt_run_defaults,
#         task_id='upload_edr_report',
#         name='upload_edr_report',
#         arguments=[edr_report],
#     )
#
# def get_config_params():
#     @task()
#     def get_dbt_mode_parameter():
#         context = get_current_context()
#         is_full_refresh = context["params"]["is_full_refresh"]
#         print(f"is_full_refresh: {is_full_refresh}")
#         print(f"type: {type(is_full_refresh)}")
#         mode = "--full-refresh" if is_full_refresh else ""
#         # Construct the run commands with mode variable
#         run_stg = construct_dbt_run_command("stg", mode)
#         run_dw = construct_dbt_run_command("dw", mode)
#         run_dm = construct_dbt_run_command("dm", mode)
#         return run_stg, run_dw, run_dm
#
#     airbyte_sync >> get_dbt_mode_parameter() >> Transformations >> edr_report
#
#
# get_config_params()
