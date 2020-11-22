import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from dateutil.relativedelta import relativedelta


###############################################################################
# PARAMETERS

DATE = datetime(2020, 11, 22, 1, 1)


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
# CLASSES

class TimeDiff(BaseOperator):
    @apply_defaults
    def __init__(
            self,
            date,
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.date = date

    def execute(self, context):
        diff = relativedelta(self.date, datetime.now())
        message = ""
        if diff.years != 0: message += f"{diff.years} annos"
        if diff.months != 0: message += f"{diff.months} meses" 
        if diff.days != 0: message += f"{diff.days} dias" 
        if diff.hours != 0: message += f"{diff.hours} horas" 
        if diff.minutes != 0: message += f"{diff.minutes} minutos" 
        self.log.info(message)
        return message


###############################################################################
# FUNCTIONS


###############################################################################
# SCRIPT

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

time_task = TimeDiff(task_id='timediff', date=DATE, dag=dag)

start >> time_task >> end



# Un hook es una interfaz para interactuar con un servicio externo (ofreciendo metodos,
# facilidades en la conexion...). Hay hooks para multiples servicios de terceros: gcp, s3, hdfs...

# La diferencia con las conexiones es que las conexiones simplemente son una forma
# de guardar metodos y datos de autenticacion de servicios externos.
# Los hooks usan internamente (en sus metodos) conexiones para poder almacenar y facilitar el acceso
# a los servicios correspondientes
