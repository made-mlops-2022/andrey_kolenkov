FROM python:3.10

COPY . /home

RUN cd /home && \
    pip install -r requirements.txt

ENTRYPOINT ["python", "/home/validator.py"]
