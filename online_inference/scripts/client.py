import requests
import pandas as pd

def main():
    data = pd.read_csv("some_data.csv")
    del data["condition"]
    feature_names = list(data.columns)
    features = data.values.tolist()
    json_dict = {"feature_names" : feature_names, "features" : features, "model" : "LOGREG"}
    response = requests.get("http://127.0.0.1:14565/predict", json=json_dict)
    print(response.json())
    return response

if __name__ == "__main__":
    main()

