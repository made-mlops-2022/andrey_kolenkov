# Коленков Андрей, ML-21, ДЗ1

# Проделанная работа:
Используется датасет https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
- Датасет скачивается в ./data/data.csv с помощью скрипта
- Выполнено EDA в ./EDA/EDA.ipynb
- В ./src/train.py написан код для обучения модели
- В ./src/prepare.py написан код для подготовки данных с помощью ColumnTransformer и для сохранения выгодных параметров модели в конфиг
- В ./src/predict.py написан код для получения предсказаний
- В ./test/test.py тестируется работа модели на предмет отсутствия исключений
- Зависимости прописаны в ./venv/requirements.txt
- В проекте используется форматтер autopep8, линтеры pylint, flake8, которые запускаются в github actions
- Написан скрипт, который прогоняет полностью весь процесс от скачивания датасета до предсказаний и тестов

# Структура проекта:

```
.
├── artifacts
├── config
│   ├── config1.json
│   ├── config2.json
│   └── make_params.py
├── data
├── EDA
│   └── EDA.ipynb
├── make.sh
├── predictions
├── README.md
├── report
├── src
│   ├── config_data.py
│   ├── predict.py
│   ├── prepare.py
│   ├── train.py
│   └── utils.py
├── test
│   └── test.py
```

# Установка (запуск из ml_project)
    ```
    python3 -m venv ./venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r ./venv/requirements.txt
    ```

# Запуск
Можно запустить сразу весь пайплайн с помощью скрипта:
```
bash make.sh *конфиг* *флаг на прод*
```
Например:
```
bash make.sh config1.json prod
```
`конфиг` - имя конфига из каталога config, `флаг на прод` - флаг (значение - `prod`), который активирует venv (в github actions не нужен)

# Запуск по отдельности
Каждую цель можно запустить отдельно:
```
cd src
python3 *модуль* *конфиг*
```
Модули: `prepare.py` `prepare.py` `predict.py`
Относительный путь до конфига: `../config/config1.json` `../config/config2.json`



