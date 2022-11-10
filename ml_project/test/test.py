import unittest
import sys
sys.path.insert(0, '../src/')


class Test(unittest.TestCase):
    def test_train(self):
        sys.argv += ["../config/config1.json"]
        from train import Train
        try:
            trainer = Train()
            trainer.train()
            trainer.save_models()
        except Exception as ex:
            self.fail(f"Train failed: {ex}")

    def test_predict(self):
        sys.argv += ["../config/config1.json"]
        from predict import Predict
        try:
            predictor = Predict()
            predictor.predict()
            predictor.save_metrics()
        except Exception as ex:
            self.fail(f"Train failed: {ex}")


if __name__ == "__main__":
    unittest.main()
