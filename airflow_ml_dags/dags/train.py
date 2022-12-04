from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from docker.types import Mount
from airflow.utils.email import send_email
import os
from common import email_alert, default_args

mount = Mount(source="../data", target="/data", type="bind")

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
        mounts=[mount]
    )

    data_splitter = DockerOperator(
        image="airflow-data-splitter",
        command="--data-dir  /data/ready/{{ ds }} --train-dir /data/train/{{ ds }} --val-dir /data/val/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-data-splitter",
        do_xcom_push=False,
        auto_remove=True,
        mounts=[mount]
    )

    trainer = DockerOperator(
        image="airflow-trainer",
        command="--data-dir  /data/train/{{ ds }} --result-dir /data/models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-trainer",
        do_xcom_push=False,
        auto_remove=True,
        mounts=[mount]
    )

    validator = DockerOperator(
        image="airflow-validator",
        command="--data_dir  /data/val/{{ ds }} --model-dir /data/models --result-dir /data/metrics/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-validator",
        do_xcom_push=False,
        auto_remove=True,
        mounts=[mount]
    )

    wait_data >> preprocessor >> data_splitter >> trainer >> validator
