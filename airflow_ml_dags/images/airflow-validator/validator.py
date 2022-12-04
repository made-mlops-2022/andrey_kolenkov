import pandas as pd
import numpy as np
import pickle
import click
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


@click.command("validator")
@click.option("--data-dir", type=click.Path())
@click.option("--model-dir", type=click.Path())
@click.option("--result-dir", type=click.Path())
def validate(data_dir, model_dir, result_dir):
    os.makedirs(result_dir, exist_ok=True)
    X = pd.read_csv(f"{data_dir}/X_test.csv")
    Y = pd.read_csv(f"{data_dir}/y_test.csv")

    with open(f"{model_dir}/model", 'rb') as file:
        model = pickle.load(file)

    y_pred = model.predict(X)

    accuracy = accuracy_score(y_true, y_pred)

    with open(f"{result_dir}/accuracy.txt", w) as file:
        file.write("Accuracy: {accuracy}")

if __name__ == "__main__":
    validate()
