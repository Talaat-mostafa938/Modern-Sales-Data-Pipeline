from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 25),  # Change as needed
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=15),
}

with DAG(
    'dbt_dag',
    default_args=default_args,
    description='Run dbt models via Docker container',
    schedule_interval='@daily',
    catchup=False,
    tags=['dbt'],
) as dag:

    DBT_DIR = "/usr/app/project_dbt"
    DBT_CONTAINER = "dbt-container"

    # المهمة الأولى: تشغيل نماذج dbt داخل الحاوية المخصصة
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=(
            f"docker exec {DBT_CONTAINER} sh -c 'set -e; cd {DBT_DIR} && "
            f"dbt run --project-dir {DBT_DIR} --profiles-dir {DBT_DIR}'"
        ),
    )

    # المهمة الثانية: اختبار البيانات بعد التحويل
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=(
            f"docker exec {DBT_CONTAINER} sh -c 'set -e; cd {DBT_DIR} && "
            f"dbt test --project-dir {DBT_DIR} --profiles-dir {DBT_DIR}'"
        ),
    )

    # تحديد الاعتمادية (dbt_run يجب أن ينتهي أولاً)
    dbt_run >> dbt_test