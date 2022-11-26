import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
import sys
sys.path.append("../restapi_app")
from app import FASTAPI_APP


class TestFastAPIApp(unittest.TestCase):

    def test_predict(self):
        class model_mock:
            def predict(self):
                return 1
        with patch.dict("app.MODELS", {"LOGREG": model_mock}):
            client = TestClient(FASTAPI_APP)
            features = [[69.0, 1.0, 0.0, 160.0, 234.0, 1.0, 2.0, 131.0, 0.0, 0.1, 1.0, 1.0, 0.0], [69.0, 0.0, 0.0, 140.0, 239.0, 0.0,
                                                                                               0.0, 151.0, 0.0, 1.8, 0.0, 2.0, 0.0], [66.0, 0.0, 0.0, 150.0, 226.0, 0.0, 0.0, 114.0, 0.0, 2.6, 2.0, 0.0, 0.0]]
            feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                     'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
            response = client.get(
                "/predict",
                {"features": features, "feature_names": feature_names, "model": "LOGREG"})
            self.assertEqual(response.status_code, 200)

    def test_health(self):
        with patch("app.MODELS"):
            client = TestClient(FASTAPI_APP)
            response = client.get("/health")
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
