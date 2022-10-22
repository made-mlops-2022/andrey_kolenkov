from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

CONFIG_PATH = "../config/parameters.json"


def select_model(model_name: str):
    if model_name == "KNN":
        return KNeighborsClassifier
    if model_name == "LOGREG":
        return LogisticRegression
    raise ValueError("Incorrect model name or it has not been implemented")
