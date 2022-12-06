#!/usr/bin/env bash

set -e pipefail

export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
sudo chmod 666 /var/run/docker.sock
sudo ausearch -c 'airflow task ru' --raw | audit2allow -M my-airflowtaskru
sudo semodule -X 300 -i my-airflowtaskru.pp
sudo docker-compose build
sudo docker-compose up
