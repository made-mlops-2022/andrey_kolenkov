import logging
from config_data import Config
import pickle
import numpy as np
from sklearn.pipeline import Pipeline
from utils import select_model
import sys

logging.basicConfig(filename="../report/log.txt",
                    encoding='utf-8', format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)


class Train:
    def __init__(self):
        CONFIG_PATH = sys.argv[1]
        logging.debug("Reading config")
        with open(CONFIG_PATH, "r", encoding="utf-8") as json_file:
            config_str = json_file.read()
            self.config = Config(config_str)
        self.train_X = np.loadtxt(self.config.train_X_file_path)
        self.train_Y = np.loadtxt(self.config.train_Y_file_path)
        self.trained_models = []
        logging.debug("Config is read")

    def train(self):
        for model in self.config.model:
            logging.debug(f"Training model {model}")
            ml_model = select_model(model)

            pipeline = Pipeline(
                steps=[("model", ml_model(**self.config.model[model]))]
            )

            pipeline.fit(self.train_X, self.train_Y)
            model_artifact = pickle.dumps(pipeline)
            self.trained_models += [model_artifact]
            logging.debug(f"Model {model} is trained")

    def save_models(self):
        logging.debug("Saving trained models")
        for i, model in enumerate(self.config.model):
            with open(f"{self.config.artifact_folder_path}/{model}",
                      "wb") as file:
                pickle.dump(self.trained_models[i], file)
        logging.debug("Trained models are saved")


def main():
    trainer = Train()
    trainer.train()
    trainer.save_models()


if __name__ == "__main__":
    main()
