# Коленков Андрей, ML-21, ДЗ1

# Проделанная работа:
Используется датасет https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
- Датасет скачивается в ./data/data.csv с помощью скрипта
- Выполнено EDA в ./EDA/EDA.ipynb
- В ./src/train.py написан код для обучения модели
- В ./src/prepare_data.py написан код для подготовки данных с помощью ColumnTransformer
- В ./src/predict.py написан код для получения предсказаний
- В ./test/test.py тестируется работа модели (пока хз как, ну я сделаю)
- Для всех модулей используется один общий конфиг в ./config/parameters.json. Все модули используют модуль json, который подгружает этот конфиг и использует из него информацию
- Зависимости прописаны в ./venv/requirements.txt
- В проекте используется форматтер black, линтеры pylint, flake8, которые запускаются в github actions
