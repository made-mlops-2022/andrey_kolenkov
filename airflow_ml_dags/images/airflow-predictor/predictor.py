import pandas as pd
import numpy as np
import pickle
import click
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


@click.command("predictor")
@click.option("--data-dir", type=click.Path())
@click.option("--model-dir", type=click.Path())
@click.option("--result-dir", type=click.Path())
def predict(data_dir, model_dir, result_dir):
    os.makedirs(result_dir, exist_ok=True)
    X = pd.read_csv(f"{data_dir}/X_test.csv")

    with open(f"{model_dir}/model", 'rb') as file:
        model = pickle.load(file)

    y_pred = model.predict(X)

    df = pd.Dataframe(y_pred)
    y.to_csv(f"{result_dir}/result.csv")

if __name__ == "__main__":
    predict()
