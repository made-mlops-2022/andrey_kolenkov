from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from docker.types import Mount
from airflow.utils.email import send_email
import os
from common import email_alert, default_args, get_mount

with DAG(
    "predictor",
    default_args=default_args,
    schedule_interval="@daily"
):
    wait_data = PythonSensor(
        task_id="wait_data",
        python_callable=os.path.exists,
        op_args=["/opt/airflow/data/raw/{{ ds }}/data.csv"],
        timeout=6000,
        mode="poke",
        poke_interval=60,
        retries=100,
    )

    preprocessor = DockerOperator(
        image="airflow-preprocessor",
        command="--raw-data-dir /data/raw/{{ ds }} --output-dir /data/ready/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-preprocessor",
        do_xcom_push=False,
        auto_remove=True,
        mounts=[get_mount()]
    )

    predictor = DockerOperator(
        image="airflow-predictor",
        command="--data-dir  /data/ready/{{ ds }} --model-dir /data/models/{{ ds }} --result-dir /data/predictions/{{ ds }}]",
        network_mode="bridge",
        task_id="docker-airflow-predictor",
        do_xcom_push=False,
        auto_remove=True,
        mounts=[get_mount()]
    )

    wait_data >> preprocessor >> predictor
