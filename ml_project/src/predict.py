import logging
from config_data import Config
import pickle
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
import json
import sys
logging.basicConfig(filename="../report/log.txt", format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)


class Predict:
    def __init__(self):
        CONFIG_PATH = sys.argv[1]
        logging.debug("Reading config")
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            config_str = json_file.read()
            self.config = Config(config_str)
        self.test_X = np.loadtxt(self.config.test_X_file_path)
        self.test_Y = np.loadtxt(self.config.test_Y_file_path)
        self.predictions = []
        logging.debug("Config is read")

    def predict(self):
        for model in self.config.model:
            logging.debug(f"Model {model} is predicting")
            with open(f"{self.config.artifact_folder_path}/{model}",
                      "rb") as file:
                bytes_data = pickle.load(file)
                trained_model = pickle.loads(bytes_data)
                prediction = trained_model.predict(self.test_X)
                self.predictions += [prediction]
                np.savetxt(
                    f"{self.config.predictions_folder_path}/{model}.csv",
                    prediction
                )
            logging.debug(f"Model {model} is finished")

    def save_metrics(self):
        metrics = {}
        for i, model in enumerate(self.config.model):
            logging.debug(f"Saving metrics for model {model}")
            metrics[model] = {}
            metrics[model]["accuracy_score"] = accuracy_score(
                self.test_Y, self.predictions[i])
            metrics[model]["f1_score"] = f1_score(
                self.test_Y, self.predictions[i])
            metrics[model]["roc_auc_score"] = roc_auc_score(
                self.test_Y, self.predictions[i])
            metrics[model]["recall_score"] = recall_score(
                self.test_Y, self.predictions[i])
            logging.debug(f"Metrics for model {model} are saved")
        print(metrics)
        with open(self.config.metrics_path, "w", encoding="utf-8") as file:
            json.dump(metrics, file)
        logging.debug(f"All metrix are written to {self.config.metrics_path}")


def main():
    predictor = Predict()
    predictor.predict()
    predictor.save_metrics()


if __name__ == "__main__":
    main()
