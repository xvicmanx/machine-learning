import numpy as np
import pandas as pd
import joblib
import os.path
import decamelize
from minisom import MiniSom  

dirname = os.path.dirname(__file__)

class SOMModel:
    # Path of the file of the dataset used to train the model
    __dataset_file_path = dirname + '/' + 'dataset.csv'
    _persisted_models_dirname = 'persisted_models_data/k_means'

    def __init__(self, size = 3, sigma = 0.5,  learning_rate = 0.5):
        self.__size = size
        base = dirname + '/' + self._persisted_models_dirname + '/' + decamelize.convert(self.__class__.__name__)
        self.__model_file_path = base + "_serialized.sav"
        self.__sigma = sigma
        self.__learning_rate = learning_rate

    def train(self):
        """Trains the model by reading the data from file, preprocessing and training the model
        """
        self.__read_and_process_data()
        self.__model = self._get_model_instance()
        self.__model.train(self.__inputs, 100)

    def predict(self, item):
        """Predicts the value of the list of given values
        """
        return self.__model.winner(item)

    def load(self):
        """Loads the serialized model
        """
        self.__model = self._load_object(self.__model_file_path)

    def save(self):
        """Save a serialized version of the model to a file
        """
        self._save_object(self.__model, self.__model_file_path)

    def dataset(self):
       return pd.read_csv(self.__dataset_file_path)
    
    def _get_model_instance(self):
        return MiniSom(
            self.__size,
            self.__size,
            17,
            sigma = self.__sigma,
            learning_rate = self.__learning_rate,
        )

    def _save_object(self, obj, file_path):
        joblib.dump(obj, file_path)
    
    def _load_object(self, file_path):
        return joblib.load(file_path)

    def __read_and_process_data(self):
        self.__inputs = self.dataset().iloc[:, 1:].values