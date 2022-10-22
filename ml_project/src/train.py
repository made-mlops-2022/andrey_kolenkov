from utils import select_model, CONFIG_PATH
from sklearn.pipeline import Pipeline
import numpy as np
import pickle
import json
import logging
logging.basicConfig(filename="../report/log.txt",
                    encoding='utf-8', format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)


class Train:
    def __init__(self):
        logging.debug("Reading config")
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        self.models = self.data["model"]
        self.random_state = int(self.data["random_state"])
        self.train_X_file_path = self.data["train_X_file_path"]
        self.train_Y_file_path = self.data["train_Y_file_path"]
        self.train_X = np.loadtxt(self.train_X_file_path)
        self.train_Y = np.loadtxt(self.train_Y_file_path)
        self.artifact_folder_path = self.data["artifact_folder_path"]
        self.trained_models = []
        logging.debug("Config is read")

    def train(self):
        for model in self.models:
            logging.debug(f"Training model {model}")
            ml_model = select_model(model)

            pipeline = Pipeline(
                steps=[("model", ml_model(**self.models[model]))]
            )

            pipeline.fit(self.train_X, self.train_Y)
            model_artifact = pickle.dumps(pipeline)
            self.trained_models += [model_artifact]
            logging.debug(f"Model {model} is trained")

    def save_models(self):
        logging.debug("Saving trained models")
        for i, model in enumerate(self.models):
            with open(f"{self.artifact_folder_path}/{model}", "wb") as file:
                pickle.dump(self.trained_models[i], file)
        logging.debug("Trained models are saved")


def main():
    trainer = Train()
    trainer.train()
    trainer.save_models()


if __name__ == "__main__":
    main()
