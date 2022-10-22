#!/usr/bin/bash

ALL_FILES="./src/*.py ./test/*.py ./config/*.py"
DATASET="https://www.dropbox.com/s/3mbvhnqm3pg8kf9/heart_cleveland_upload.csv?dl=0"

source venv/bin/activate

wget -O ./data/data.csv $DATASET

pip install --upgrade pip
pip install -r ./venv/requirements.txt

black $ALL_FILES --line-length 79

flake8 $ALL_FILES
pylint $ALL_FILES --disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,invalid-name,too-many-instance-attributes

cd ./config
python make_params.py #Создается первоначальный конфиг со списком параметров, из которых хотим найти лучшие
cd ../src
python prepare.py #Скачивается и разделяетс файл с данными. В конфиге каждый список параметров заменяется на лучший параметр

cd ../test
coverage run  test.py -b
coverage report -m --omit=/usr/lib/*,/usr/local/lib/*
coverage html -d ./report/coverage_report

deactivate

