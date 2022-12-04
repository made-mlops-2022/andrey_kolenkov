import datetime
from docker.types import Mount

def email_alert(context):
    dag_run = context.get("dag_run")
    msg = "DAG failed"
    subject = f"DAG {dag_run} failed"
    send_email(to=default_args["email"], subject=subject, html_content=msg)


default_args = {
    "owner": "airflow",
    "start_date": datetime.datetime.today() - datetime.timedelta(days=7),
    "email": ["avoknelok@mail.ru"],
    "retry_delay": datetime.timedelta(minutes=5),
    "retries": 1,
    "on_failure_callback": email_alert
}


def get_mount():
    return Mount(source="/home/adefe/prog/Python/andrey_kolenkov/airflow_ml_dags/data", target="/data", type="bind")
