from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount
from airflow.utils.email import send_email
from common import email_alert, default_args, get_mount


with DAG(
    "data_generator",
    default_args=default_args,
    schedule_interval="@daily"
):
    data_generator = DockerOperator(
        image="airflow-data-generator",
        command="--output-dir /data/raw/{{ ds }}",
        do_xcom_push=False,
        network_mode="bridge",
        auto_remove=True,
        task_id="docker-airflow-data-generator",
        mounts=[get_mount()])

    data_generator
