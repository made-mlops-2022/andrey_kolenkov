import json
from dataclasses import dataclass


@dataclass
class Config:
    def __init__(self, file_path):
        with open(file_path) as file:
            self.data = json.load(file)
        self.random_state = int(self.data["random_state"])
        self.knn_model_path = self.data["knn_model_path"]
        self.logreg_model_path = self.data["logreg_model_path"]
        self.cathegory_features = self.data["cathegory_features"]
        self.number_features = self.data["number_features"]
        self.target_feature = self.data["target_feature"]
