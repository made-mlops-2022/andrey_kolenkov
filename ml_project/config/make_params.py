import json


def main():
    data = {
        "random_state": "14565",
        "input_file_path": "../data/data.csv",
        "train_X_file_path": "../data/train_X.csv",
        "train_Y_file_path": "../data/train_Y.csv",
        "test_X_file_path": "../data/test_X.csv",
        "test_Y_file_path": "../data/test_Y.csv",
        "output_model_path": "../models/ready_model.plk",
        "metrics_path": "../report/metrix.json",
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
            "KNN": {"n_neighbors": [2, 3, 4, 5, 6, 7]},
            "LOGREG": {"C": [1.0, 1.5, 2.0],
                       "max_iter": [1000]},
            "SGDC": {"alpha": [0.0001, 0.001, 0.01],
                     "l1_ratio": [0.15, 0.4, 0.7]},
        },
        "artifact_folder_path": "../artifacts",
        "predictions_folder_path": "../predictions",
    }

    with open("parameters.json", "w", encoding="utf-8") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
