import pandas as pd
import numpy as np
import os
import click


@click.command("data_generator")
@click.option("--output-dir", type=click.Path())
def generate_data(output_dir):
    os.makedirs(output_dir, exist_ok=True)

    columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
               "thalanch", "exang", "oldpeak", "slope", "ca", "thal", "condition"]
    df = pd.Dataframe(columns=columns)
    for column in columns:
        df[column] = np.random.randint(0, 200, size=1000)

    df.to_csv(f"{output_dir}/data.csv", index=False)

if __name__=="__main__":
    generate_data()
