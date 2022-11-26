import requests
import pandas as pd

def main():
    data = pd.read_csv("some_data.csv")
    del data["condition"]
    feature_names = list(data.columns)
    features = data.values.tolist()
    response = requests.get("http://127.0.0.1:14565/predict", json={"feature_names" : feature_names, "features" : features, "model" : "LOGREG"})
    print(response.json())
    return response

if __name__ == "__main__":
    main()

