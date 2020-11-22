import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta


###############################################################################
# PARAMETERS

N = 6


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

impares = []
pares = []
for i in range(1, N+1):
    if i % 2 == 0: pares.append(DummyOperator(task_id=f"task_{i}", dag=dag))
    else: impares.append(DummyOperator(task_id=f"task_{i}", dag=dag))

start >> impares
for task_par in pares:
    for task_impar in impares:
        task_impar >> task_par
    task_par >> end

