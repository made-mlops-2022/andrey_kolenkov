import click
import pandas as pd
import numpy as np
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import KNNImputer


@click.command("preprocessor")
@click.option("--raw-data-dir", type=click.Path())
@click.option("--output-dir", type=click.Path())
def preprocess(raw_data_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(f"{raw_data_dir}/data.csv")

    columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
               "thalanch", "exang", "oldpeak", "slope", "ca", "thal", "condition"]

    cathegory_features = [
        "sex",
        "cp",
        "restecg",
        "exang",
        "slope",
        "thal",
    ]
    number_features = [
        "age",
        "trestbps",
        "chol",
        "fbs",
        "thalach",
        "oldpeak",
        "ca",
    ]

    target_feature = "condition"

    ct = ColumnTransformer(
        [
            (
                "imputer",
                KNNImputer(),
                self.config.cathegory_features +
                self.config.number_features,
            ),
            ("number", StandardScaler(), self.config.number_features),
            (
                "cathegory",
                OneHotEncoder(handle_unknown="ignore"),
                self.config.cathegory_features,
            ),
        ]
    )

    df = pd.Dataframe(ct.fit_predict(df), columns=columns)
    df.to_csv(f"{output_dir}/data.csv", index=False)


if __name__ == "__main__":
    preprocess()
