from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import logging
logging.basicConfig(filename="../report/log.txt",
                    encoding="UTF-8", format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)


def select_model(model_name: str):
    logging.debug("Fabric function is called")
    if model_name == "KNN":
        return KNeighborsClassifier
    if model_name == "LOGREG":
        return LogisticRegression
    if model_name == "SGDC":
        return SGDClassifier
    raise ValueError("Incorrect model name or it has not been implemented")
