import json
from dataclasses import dataclass


@dataclass
class Config:

    def __init__(self, json_string: str):
        self.data = json.loads(json_string)
        self.random_state = int(self.data["random_state"])
        self.input_file_path = self.data["input_file_path"]
        self.train_X_file_path = self.data["train_X_file_path"]
        self.train_Y_file_path = self.data["train_Y_file_path"]
        self.test_X_file_path = self.data["test_X_file_path"]
        self.test_Y_file_path = self.data["test_Y_file_path"]
        self.output_model_path = self.data["output_model_path"]
        self.metrics_path = self.data["metrics_path"]
        self.log_path = self.data["log_path"]
        self.test_size = float(self.data["test_size"])
        self.cathegory_features = self.data["cathegory_features"]
        self.number_features = self.data["number_features"]
        self.target_feature = self.data["target_feature"]
        self.model = self.data["model"]
        self.artifact_folder_path = self.data["artifact_folder_path"]
        self.predictions_folder_path = self.data["predictions_folder_path"]
