import pandas as pd
import numpy as np
import pickle
import os
import click
from sklearn.linear_model import LogisticRegression


@click.command("trainer")
@click.option("--data-dir", type=click.Path())
@click.option("--result-dir", type=click.Path())
def train(data_dir, result_dir):
    os.makedirs(result_dir, exist_ok=True)
    X = pd.read_csv(f"{data_dir}/X_train.csv")
    Y = pd.read_csv(f"{data_dir}/y_train.csv")

    model = LogisticRegression()

    model.fit(X, y)

    with open(f"{result_dir}/model", 'wb') as file:
        pickle.dump(model, file)


if __name__ == "__main__":
    train()
