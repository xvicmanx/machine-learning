import os.path
import decamelize
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, fbeta_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class BankLeavingPredictionModel:
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.csv'

    def __init__(self):
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__
        self.__inputs_scaler = None
        self.__inputs_label_encoder = None
        self.__inputs_one_hot_encoder = None
        model_decamelized = decamelize.convert(self.model_name)

        self.__model_filename = persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
        self.__inputs_scaler_filename = persisted_models_dirname + '/' + model_decamelized + '_inputs_scaler.sav'
        self.__inputs_label_encoder_filename = persisted_models_dirname + '/' + model_decamelized + '_label_encoder.sav'
        self.__inputs_one_hot_encoder_filename = persisted_models_dirname + '/' + model_decamelized + '_one_hot_encoder.sav'

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
        inputs = self._transform_input_features(self._preprocess_inputs(pd.DataFrame(items).values))
        return self._inverse_transform_outputs(self.__model.predict(inputs))

    """Loads the serialized model
    """
    def load(self):
        self.__model = self._load_object(self.__model_filename)
        self.__inputs_scaler = self._load_object(self.__inputs_scaler_filename)
        self.__inputs_label_encoder = self._load_object(self.__inputs_label_encoder_filename)
        self.__inputs_one_hot_encoder = self._load_object(self.__inputs_one_hot_encoder_filename)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_object(self.__model, self.__model_filename)
        self._save_object(self.__inputs_scaler, self.__inputs_scaler_filename)
        self._save_object(self.__inputs_label_encoder, self.__inputs_label_encoder_filename)
        self._save_object(self.__inputs_one_hot_encoder, self.__inputs_one_hot_encoder_filename)

    def _save_object(self, obj, filename):
        joblib.dump(obj, dirname + '/' + filename)
    
    def _load_object(self, filename):
        return joblib.load(dirname + '/' + filename)

    def _get_model_instance(self):
        raise Exception('Method not implemented')

    def _preprocess_inputs(self, inputs):
        if self.__inputs_label_encoder is None:
            self.__inputs_label_encoder = LabelEncoder()
            self.__inputs_label_encoder.fit(inputs[:, 2])

        inputs[:, 2] = self.__inputs_label_encoder.transform(inputs[:, 2])

        if self.__inputs_one_hot_encoder is None:
            self.__inputs_one_hot_encoder = ColumnTransformer(
                transformers = [('cat', OneHotEncoder(), [1])],
                remainder = 'passthrough',
            )
            self.__inputs_one_hot_encoder.fit(inputs)

        return self.__inputs_one_hot_encoder.transform(inputs)

    def _preprocess_outputs(self, outputs):
        return outputs

    def _transform_input_features(self, inputs):
        if self.__inputs_scaler is None:
            self.__inputs_scaler = StandardScaler()
            return self.__inputs_scaler.fit_transform(inputs)

        return self.__inputs_scaler.transform(inputs)
    
    def _transform_outputs(self, outputs):
        return outputs

    def _inverse_transform_outputs(self, transformed_outputs):
        return transformed_outputs

    def __read_and_process_data(self):
        dataset = pd.read_csv(dirname + '/' + self.__dataset_filename)
        inputs_train, inputs_test, outputs_train, outputs_test = train_test_split(
          self._preprocess_inputs(dataset.iloc[:, 3:-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1 / 5,
          random_state = 0,
        )
        self.__inputs_train = self._transform_input_features(inputs_train)
        self.__outputs_train = self._transform_outputs(outputs_train)
        self.__inputs_test = inputs_test
        self.__outputs_test = outputs_test

    def __evaluate(self):
        predictions = self.__model.predict(self._transform_input_features(self.__inputs_test))
        return {
            'accuracy_score': accuracy_score(
                self._transform_outputs(self.__outputs_test),
                predictions,
            ),
            'confusion_matrix': confusion_matrix(
                self._transform_outputs(self.__outputs_test),
                predictions,
            ),
            'f0.5_score': fbeta_score(
                self._transform_outputs(self.__outputs_test),
                predictions,
                beta = 0.5,
            ),
            'f1_score': fbeta_score(
                self._transform_outputs(self.__outputs_test),
                predictions,
                beta = 1.0,
            ),
            'f2_score': fbeta_score(
                self._transform_outputs(self.__outputs_test),
                predictions,
                beta = 2.0,
            ),
        }