import json

def main():
    data = {
            "input_file_path" : "../data/data.csv",
            "output_model_path":"../models/ready_model.plk",
            "metrics_path":"../report/metrix.json",
            "cathegory_features" : ["sex",
                                    "cp",
                                    "restecg",
                                    "exang",
                                    "slope",
                                    "thal",],
            "number_features" : ["age",
                                "trestbps",
                                "chol",
                                "fbs",
                                "thalach",
                                "oldpeak",
                                "ca",],
            "target_feature" : "condition",
            }

    with open("parameters.json", "w") as file:
        json.dump(data, file)

if __name__=="__main__":
    main()
