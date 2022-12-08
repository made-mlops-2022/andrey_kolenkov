import unittest
import pandas as pd
from unittest.mock import patch
from fastapi.testclient import TestClient
import sys
sys.path.append("../restapi_app")
from app import FASTAPI_APP


class TestFastAPIApp(unittest.TestCase):

    def test_predict(self):
        class model_mock:
            def predict(x):
                return [1 for _ in x]
        with patch.dict("app.MODELS", {"LOGREG": model_mock}):
            data = pd.read_csv("some_data.csv")
            data = data.drop("condition", axis=1)
            feature_names = list(data.columns)
            features = data.values.tolist()
            json_dict = {"feature_names" : feature_names, "features" : features, "model_type" : "LOGREG"}
            client = TestClient(FASTAPI_APP)
            response = client.get(
                "/predict",
                json=json_dict)
            self.assertEqual(response.status_code, 200)

    def test_health(self):
        with patch("app.MODELS"):
            client = TestClient(FASTAPI_APP)
            response = client.get("/health")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["status"], 0)


if __name__ == "__main__":
    unittest.main()
