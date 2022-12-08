FROM fedora:36

COPY . /home

RUN cd /home/ && \
    dnf upgrade -y --refresh && \
    dnf -y install python && \
    dnf -y install pip && \
    pip install -r /home/requirements.txt

CMD ["uvicorn", "--app-dir", "/home/restapi_app/", "--host", "0.0.0.0", "--port", "14565", "app:FASTAPI_APP"]
