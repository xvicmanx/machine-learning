import os.path
import decamelize
import pandas as pd
import numpy as np


from core.regression_model import RegressionModel

dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class MovieRatePredictionModel(RegressionModel):
    def __init__(self):
        super().__init__()

        base = dirname + '/' + persisted_models_dirname + '/' + decamelize.convert(self.__class__.__name__)
        
        self.__model_file_path = base + "_serialized.sav"


    def load(self):
        """Loads the serialized model
        """
        self._load_model(self.__model_file_path)

    def save(self):
        """Save a serialized version of the model to a file
        """
        self._save_model(self.__model_file_path)

    def _split_data(self):
        dataset_base = dirname + '/datasets/ml-100k/'
        training_set = self.__read_dataset(dataset_base + 'u1.base')
        test_set = self.__read_dataset(dataset_base + 'u1.test')

        total_of_users = int(max(max(training_set[:, 0], ), max(test_set[:, 0])))
        total_of_movies = int(max(max(training_set[:, 1], ), max(test_set[:, 1])))

        training_set = self.__convert_to_array(
            training_set,
            total_of_users,
            total_of_movies,
        )
        test_set = self.__convert_to_array(
            test_set,
            total_of_users,
            total_of_movies,
        )

        return training_set, training_set, test_set, test_set

    def __convert_to_array(self, data, total_of_users, total_of_movies):
        result = np.zeros((total_of_users, total_of_movies))
        for user_id in range(1, total_of_users + 1):
            indexes = data[:, 0] == user_id
            movies = data[:, 1][indexes]
            ratings = data[:, 2][indexes]
            result[user_id - 1, movies - 1] = ratings
        return result

    def __read_dataset(self, file_path):
        data = pd.read_csv(file_path, delimiter = '\t')
        return np.array(data, dtype = 'int')

    def __read_dat_file(self, file_path):
        return pd.read_csv(
            file_path,
            sep = '::',
            header = None,
            engine = 'python',
            encoding = 'latin-1',
        )
