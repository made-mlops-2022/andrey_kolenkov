import logging
from config_data import Config
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
import sys
logging.basicConfig(filename="../report/log.txt",
                    encoding='utf-8', format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)


class Prepare:
    def __init__(self):
        CONFIG_PATH = sys.argv[1]
        logging.debug("Reading config")
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            config_str = json_file.read()
            self.config = Config(config_str)
        self.csv_data = pd.read_csv(self.config.input_file_path)
        self.X = self.csv_data.drop("condition", axis=1)
        self.Y = self.csv_data["condition"]
        self.ct = ColumnTransformer(
            [
                (
                    "imputer",
                    KNNImputer(),
                    self.config.cathegory_features +
                    self.config.number_features,
                ),
                ("number", StandardScaler(), self.config.number_features),
                (
                    "cathegory",
                    OneHotEncoder(handle_unknown="ignore"),
                    self.config.cathegory_features,
                ),
            ]
        )
        logging.debug("Config is read")

    def prepare_features(self):
        logging.debug("Start preparing features")
        np_X = self.ct.fit_transform(self.X)
        np_Y = self.Y.to_numpy()
        X_train, X_test, Y_train, Y_test = train_test_split(
            np_X,
            np_Y,
            test_size=self.config.test_size,
            random_state=self.config.random_state,
        )
        np.savetxt(self.config.train_X_file_path, X_train)
        np.savetxt(self.config.test_X_file_path, X_test)
        np.savetxt(self.config.train_Y_file_path, Y_train)
        np.savetxt(self.config.test_Y_file_path, Y_test)
        logging.debug("New feature files are saved")


def main():
    preparator = Prepare()
    preparator.prepare_features()


if __name__ == "__main__":
    main()
