import json
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
from sklearn.model_selection import GridSearchCV

from utils import select_model


CONFIG_PATH = "../config/parameters.json"


class Prepare:
    def __init__(self):
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        self.random_state = int(self.data["random_state"])
        self.test_size = float(self.data["test_size"])
        self.cathegory_features = self.data["cathegory_features"]
        self.number_features = self.data["number_features"]
        self.target_feature = self.data["target_feature"]
        self.models = self.data["model"]
        self.train_X_file_path = self.data["train_X_file_path"]
        self.train_Y_file_path = self.data["train_Y_file_path"]
        self.test_X_file_path = self.data["test_X_file_path"]
        self.test_Y_file_path = self.data["test_Y_file_path"]
        self.csv_data = pd.read_csv(self.data["input_file_path"])
        self.X = self.csv_data.drop("condition", axis=1)
        self.Y = self.csv_data["condition"]
        self.ct = ColumnTransformer(
            [
                (
                    "imputer",
                    KNNImputer(),
                    self.cathegory_features + self.number_features,
                ),
                ("number", StandardScaler(), self.number_features),
                (
                    "cathegory",
                    OneHotEncoder(handle_unknown="ignore"),
                    self.cathegory_features,
                ),
            ]
        )

    def prepare_features(self):
        np_X = self.ct.fit_transform(self.X)
        np_Y = self.Y.to_numpy()
        X_train, X_test, Y_train, Y_test = train_test_split(
            np_X,
            np_Y,
            test_size=self.test_size,
            random_state=self.random_state,
        )
        np.savetxt(self.train_X_file_path, X_train)
        np.savetxt(self.test_X_file_path, X_test)
        np.savetxt(self.train_Y_file_path, Y_train)
        np.savetxt(self.test_Y_file_path, Y_test)

    def update_parameters(self):
        for model in self.models:
            ml_model = select_model(model)

            pipeline = Pipeline(
                steps=[("prepare", self.ct), ("model", ml_model())]
            )

            parameters = {}
            for parameter in self.models[model]:
                parameters[f"model__{parameter}"] = self.models[model][
                    parameter
                ]

            gridsearch = GridSearchCV(pipeline, parameters).fit(self.X, self.Y)

            for key, value in gridsearch.best_params_.items():
                ind = key.find("__")
                key = key[ind + 2 :]
                self.models[model][key] = value
        with open(CONFIG_PATH, "w", encoding="utf-8") as json_file:
            json.dump(self.data, json_file)


def main():
    preparator = Prepare()
    preparator.prepare_features()
    preparator.update_parameters()


if __name__ == "__main__":
    main()
