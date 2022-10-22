import json
import pickle
import numpy as np
from sklearn.pipeline import Pipeline

from utils import select_model, CONFIG_PATH


class Train:
    def __init__(self):
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        self.random_state = int(self.data["random_state"])
        self.models = self.data["model"]
        self.train_X_file_path = self.data["train_X_file_path"]
        self.train_Y_file_path = self.data["train_Y_file_path"]
        self.train_X = np.loadtxt(self.train_X_file_path)
        self.train_Y = np.loadtxt(self.train_Y_file_path)
        self.artifact_folder_path = self.data["artifact_folder_path"]
        self.trained_models = []

    def train(self):
        for model in self.models:
            ml_model = select_model(model)

            pipeline = Pipeline(
                steps=[("model", ml_model(**self.models[model]))]
            )

            pipeline.fit(self.train_X, self.train_Y)
            model_artifact = pickle.dumps(pipeline)
            self.trained_models += [model_artifact]

    def save_models(self):
        for i, model in enumerate(self.models):
            with open(f"{self.artifact_folder_path}/{model}", "wb") as file:
                pickle.dump(self.trained_models[i], file)


def main():
    trainer = Train()
    trainer.train()
    trainer.save_models()


if __name__ == "__main__":
    main()
