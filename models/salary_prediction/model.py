import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os.path 

# import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)

class SalaryPredictionModel:
    # File to stored the serialized version of the model 
    __model_filename = dirname + '/salary_prediction_model_serialized.sav'
    # File of the dataset used to train the model
    __dataset_filename = dirname + '/salary.csv'

    """Trains the model by reading the data from file, preprocessing and training the model
    """
    def train(self):
        self.__read_data()
        self.__model = LinearRegression()
        self.__model.fit(self.__X_train, self.__y_train)
        return self.__evaluate()

    """Predicts the value of the list of given values
    """
    def predict(self, items):
        return self.__model.predict(items)

    """Loads the serialized model
    """
    def load(self):
        self.__model = joblib.load(self.__model_filename)

    """Save a serialzed version of the model to a file
    """
    def save(self):
        joblib.dump(self.__model, self.__model_filename)

    def __read_data(self):
        dataset = pd.read_csv(self.__dataset_filename)
        X_train, X_test, y_train, y_test = train_test_split(
          dataset.iloc[:, :-1].values,
          dataset.iloc[:, -1].values,
          test_size = 1/3,
          random_state = 0,
        )
        self.__X_train = X_train
        self.__X_test = X_test
        self.__y_train = y_train
        self.__y_test = y_test

    def __evaluate(self):
      y_pred = self.__model.predict(self.__X_test)
      return { 'r2_score': str(r2_score(self.__y_test, y_pred)) }
