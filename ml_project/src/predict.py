import json
import pickle
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score

from utils import CONFIG_PATH


class Predict:
    def __init__(self):
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        self.random_state = int(self.data["random_state"])
        self.models = self.data["model"]
        self.test_X_file_path = self.data["test_X_file_path"]
        self.test_Y_file_path = self.data["test_Y_file_path"]
        self.test_X = np.loadtxt(self.test_X_file_path)
        self.test_Y = np.loadtxt(self.test_Y_file_path)
        self.artifact_folder_path = self.data["artifact_folder_path"]
        self.predictions_folder_path = self.data["predictions_folder_path"]
        self.metrix_path = self.data["metrics_path"]
        self.predictions = []

    def predict(self):
        for model in self.models:
            with open(f"{self.artifact_folder_path}/{model}", "rb") as file:
                bytes_data = pickle.load(file)
                trained_model = pickle.loads(bytes_data)
                prediction = trained_model.predict(self.test_X)
                self.predictions += [prediction]
                np.savetxt(
                    f"{self.predictions_folder_path}/{model}.csv", prediction
                )

    def save_metrics(self):
        metrics = {}
        for i, model in enumerate(self.models):
            metrics[model] = {}
            metrics[model]["accuracy_score"] = accuracy_score(
                self.test_Y, self.predictions[i])
            metrics[model]["f1_score"] = f1_score(
                self.test_Y, self.predictions[i])
            metrics[model]["roc_auc_score"] = roc_auc_score(
                self.test_Y, self.predictions[i])
            metrics[model]["recall_score"] = recall_score(
                self.test_Y, self.predictions[i])
        print(metrics)
        with open(self.metrix_path, "w", encoding="utf-8") as file:
            json.dump(metrics, file)


def main():
    predictor = Predict()
    predictor.predict()
    predictor.save_metrics()


if __name__ == "__main__":
    main()
