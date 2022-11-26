import os
import pickle
import pandas as pd
from datatypes import FeaturesModel, StatusModel, PredictResultModel
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import KNNImputer
from config_data import Config
import sys
from fastapi import FastAPI

FASTAPI_APP = FastAPI()

CONFIG_PATH = os.getenv("CONFIG_PATH") if os.getenv("CONFIG_PATH") else "/home/adefe/prog/Python/andrey_kolenkov/online_inference/config/config.json"

MODELS = {}
CONFIG = Config(CONFIG_PATH)


@FASTAPI_APP.on_event("startup")
def prepare_models():
    global MODELS
    with open(f"{CONFIG.knn_model_path}", "rb") as file:
        bytes_data = pickle.load(file)
        MODELS["KNN"] = pickle.loads(bytes_data)
    with open(f"{CONFIG.logreg_model_path}", "rb") as file:
        bytes_data = pickle.load(file)
        MODELS["LOGREG"] = pickle.loads(bytes_data)


@FASTAPI_APP.get("/predict", response_model=PredictResultModel)
def predict(data : FeaturesModel):
    features = pd.DataFrame(data.features, columns=data.feature_names)
    if data.model_type == "KNN":
        model = MODELS["KNN"]
    if data.model_type == "LOGREG":
        model = MODELS["LOGREG"]

    ct = ColumnTransformer(
        [
            (
                "imputer",
                KNNImputer(),
                CONFIG.cathegory_features +
                CONFIG.number_features,
            ),
            ("number", StandardScaler(), CONFIG.number_features),
            (
                "cathegory",
                OneHotEncoder(handle_unknown="ignore"),
                CONFIG.cathegory_features,
            ),
        ]
    )

    X = ct.fit_transform(features)

    result = model.predict(X)
    return PredictResultModel(result=result)


@FASTAPI_APP.get("/health", response_model=StatusModel)
def health():
    status = True
    if len(MODELS) != 2:
        status = False
    if list(MODELS.keys()) != ["KNN", "LOGREG"]:
        status = False
    return StatusModel(status=status)
