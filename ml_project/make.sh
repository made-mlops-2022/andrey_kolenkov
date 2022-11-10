#!/usr/bin/bash

set -o pipefail

ALL_FILES="./src/*.py ./test/*.py ./config/*.py"
DATASET="https://www.dropbox.com/s/3mbvhnqm3pg8kf9/heart_cleveland_upload.csv?dl=0"
CONFIG_PATH="../config/"$1
ON_PROD=$2

if [ "$ON_PROD" == "prod" ]
then
  source venv/bin/activate
fi

wget -O ./data/data.csv $DATASET

pip install --upgrade pip
pip install -r ./venv/requirements.txt

autopep8 $ALL_FILES --in-place --max-line-length 79

flake8 $ALL_FILES
pylint $ALL_FILES --disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,invalid-name,too-many-instance-attributes,logging-fstring-interpolation,wrong-import-order,too-few-public-methods,import-outside-toplevel,broad-except

cd ./config
#python3 make_params.py $CONFIG_PATH #Создается первоначальный конфиг со списком параметров, из которых хотим найти лучшие, не используется

cd ..
touch ./report/log.txt

cd ./src
python3 prepare.py $CONFIG_PATH #Скачивается и разделяетс файл с данными. В конфиге каждый список параметров заменяется на лучший параметр
python3 train.py $CONFIG_PATH #Обучается и сохраняется как артифакт каждая модель из конфига
python3 predict.py $CONFIG_PATH #Сохраняются предсказания для тестовой выборки и выводится и сохраняется accuracy_score

cd ../test
coverage run test.py
coverage report -m --omit=/usr/lib/*,/usr/local/lib/*
coverage html -d ../report/coverage_report


if [ "$ON_PROD" == "prod" ]
then
  deactivate
fi


