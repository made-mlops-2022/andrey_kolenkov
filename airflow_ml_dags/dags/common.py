from datetime import datetime, timedelta


def email_alert(context):
    dag_run = context.get("dag_run")
    msg = "DAG failed"
    subject = f"DAG {dag_run} failed"
    send_email(to=default_args["email"], subject=subject, html_content=msg)


default_args = {
    "owner": "Airflow",
    "start_date": datetime.now(),
    "email": ["avoknelok@mail.ru"],
    "retry_delay" = timedelta(minutes=30)
    "retries": 1,
    "on_failure_callback": email_alert
}
