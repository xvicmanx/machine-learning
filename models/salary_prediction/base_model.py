import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import os.path
import decamelize

# import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class BaseSalaryPredictionModel:
    # File of the dataset used to train the model
    __dataset_filename = 'salary.csv'

    def __init__(self):
        # File to stored the serialized version of the model 
        self.__model_filename = persisted_models_dirname + '/' + decamelize.convert(self.__class__.__name__) + "_serialized.sav"

    """Trains the model by reading the data from file, preprocessing and training the model
    """
    def train(self):
        self.__read_and_process_data()
        self.__model = self._get_model_instance()
        self.__model.fit(self.__inputs_train, self.__outputs_train)
        return self.__evaluate()

    """Predicts the value of the list of given values
    """
    def predict(self, items):
        return self.__model.predict(self._preprocess_inputs(items))

    """Loads the serialized model
    """
    def load(self):
        self.__model = self._load_object(self.__model_filename)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_object(self.__model, self.__model_filename)

    def _save_object(self, obj, filename):
        joblib.dump(obj, dirname + '/' + filename)
    
    def _load_object(self, filename):
        return joblib.load(dirname + '/' + filename)

    def _get_model_instance(self):
        raise Exception('Method not implemented')

    def _preprocess_inputs(self, inputs):
        return inputs

    def _preprocess_outputs(self, outputs):
        return outputs

    def __read_and_process_data(self):
        dataset = pd.read_csv(dirname + '/' + self.__dataset_filename)
        inputs_train, inputs_test, outputs_train, outputs_test = train_test_split(
          self._preprocess_inputs(dataset.iloc[:, :-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1/3,
          random_state = 0,
        )
        self.__inputs_train = inputs_train
        self.__inputs_test = inputs_test
        self.__outputs_train = outputs_train
        self.__outputs_test = outputs_test

    def __evaluate(self):
      predictions = self.__model.predict(self.__inputs_test)
      return { 'r2_score': str(r2_score(self.__outputs_test, predictions)) }
