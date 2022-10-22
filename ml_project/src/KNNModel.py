from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


class Model:
    def __init__(self, X, Y):
        self.model = KNeighborsClassifier()
