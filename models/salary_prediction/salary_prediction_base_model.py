import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import os.path
import decamelize

import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)

class BaseSalaryPredictionModel:
    # File of the dataset used to train the model
    __dataset_filename = 'salary.csv'
    _persisted_models_dirname = 'persisted_models_data'

    def __init__(self):
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__
        
        model_decamelized = decamelize.convert(self.model_name)

        self.__model_filename = self._persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
        self.__model_plot_filename = self._persisted_models_dirname + '/' + model_decamelized + "_plot.png"

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
        inputs = self._transform_input_features(self._preprocess_inputs(items))
        return self._inverse_transform_outputs(self.__model.predict(inputs))

    """Loads the serialized model
    """
    def load(self):
        self.__model = self._load_object(self.__model_filename)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_object(self.__model, self.__model_filename)
        self.__plot()

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

    def _transform_input_features(self, inputs):
        return inputs
    
    def _transform_outputs(self, outputs):
        return outputs

    def _inverse_transform_outputs(self, transformed_outputs):
        return transformed_outputs

    def __read_and_process_data(self):
        dataset = pd.read_csv(dirname + '/' + self.__dataset_filename)
        inputs_train, inputs_test, outputs_train, outputs_test = train_test_split(
          self._preprocess_inputs(dataset.iloc[:, :-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1/3,
          random_state = 0,
        )
        self.__inputs_train = self._transform_input_features(inputs_train)
        self.__outputs_train = self._transform_outputs(outputs_train)
        self.__inputs_test = inputs_test
        self.__outputs_test = outputs_test

    def __evaluate(self):
      predictions = self.__model.predict(self._transform_input_features(self.__inputs_test))
      return { 'r2_score': str(r2_score(self._transform_outputs(self.__outputs_test), predictions)) }

    def __plot(self):
        inputs_grid = np.arange(min(
            self.__inputs_test),
            max(self.__inputs_test),
            0.01
        )
        inputs_grid = inputs_grid.reshape(len(inputs_grid), 1)
        plt.scatter(
            self.__inputs_test,
            self.__outputs_test,
            color = 'red'
        )
        predictions = self._inverse_transform_outputs(self.__model.predict(self._transform_input_features(inputs_grid)))
        plt.plot(
            inputs_grid,
            predictions,
            color = 'blue'
        )
        plt.title('Salary prediction (' + self.model_name + ')')
        plt.xlabel('Years of experience')
        plt.ylabel('Salary')
        plt.savefig(dirname + '/' + self.__model_plot_filename)
        plt.clf()