import pandas as pd
import numpy as np
import os
import click
from sklearn.model_selection import train_test_split


@click.command("data_splitter")
@click.option("--data-dir", type=click.Path())
@click.option("--train-dir", type=click.Path())
@click.option("--val-dir", type=click.Path())
def split(data_dir, train_dir, val_dir):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    df = pd.read_csv(f"{data_dir}/data.csv")

    Y = df["condition"]
    X = df.drop("condition", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.25, random_state=14565)

    X_train.to_csv(f"{train_dir}/X_train.csv", index=False)
    y_train.to_csv(f"{train_dir}/y_train.csv", index=False)
    X_test.to_csv(f"{val_dir}/X_test.csv", index=False)
    y_test.to_csv(f"{val_dir}/y_test.csv", index=False)


if __name__ == "__main__":
    split()
