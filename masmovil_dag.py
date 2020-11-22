import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


###############################################################################
# PARAMETERS



###############################################################################
# DAG

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

dag = DAG(dag_id='test',
          schedule_interval="00 3 * * *",
          catchup=False,
          default_args=default_args)


###############################################################################
# FUNCTIONS


###############################################################################
# SCRIPT

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end
