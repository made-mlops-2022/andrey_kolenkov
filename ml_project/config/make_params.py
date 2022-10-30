import logging
import json
import sys
CONFIG_PATH = sys.argv[1]
logging.basicConfig(filename="../report/log.txt",
                    encoding='utf-8', format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)


def main():
    logging.debug("Creating basic config")
    data = {
        "random_state": "14565",
        "input_file_path": "../data/data.csv",
        "train_X_file_path": "../data/train_X.csv",
        "train_Y_file_path": "../data/train_Y.csv",
        "test_X_file_path": "../data/test_X.csv",
        "test_Y_file_path": "../data/test_Y.csv",
        "output_model_path": "../models/ready_model.plk",
        "metrics_path": "../report/metrics.json",
        "log_path": "../report/log.txt",
        "test_size": "0.25",
        "cathegory_features": [
            "sex",
            "cp",
            "restecg",
            "exang",
            "slope",
            "thal",
        ],
        "number_features": [
            "age",
            "trestbps",
            "chol",
            "fbs",
            "thalach",
            "oldpeak",
            "ca",
        ],
        "target_feature": "condition",
        "model": {
            "KNN": {"n_neighbors": 3},
            "LOGREG": {"C": 1.0,
                       "max_iter": 1000},
            "SGDC": {"alpha": 0.001,
                     "l1_ratio": 0.4},
        },
        "artifact_folder_path": "../artifacts",
        "predictions_folder_path": "../predictions",
    }
    logging.debug("Writing basic config")
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    logging.debug("Basic config is created")


if __name__ == "__main__":
    main()
