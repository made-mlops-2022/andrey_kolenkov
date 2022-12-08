import json
import sys
CONFIG_PATH = sys.argv[1]


def main():
    data = {
        "random_state": "14565",
        "knn_model_path": "../models/KNN",
        "logreg_model_path": "../models/LOGREG",
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
    }
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
