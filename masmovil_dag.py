import airflow
from airflow import DAG
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


