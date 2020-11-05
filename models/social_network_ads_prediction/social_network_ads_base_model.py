import os.path
import decamelize
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class SocialNetworkAdsPredictionModel:
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.csv'

    def __init__(self):
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__
        self.__inputs_scaler = None
        model_decamelized = decamelize.convert(self.model_name)

        self.__model_filename = persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
        self.__inputs_scaler_filename = persisted_models_dirname + '/' + model_decamelized + '_inputs_scaler.sav'
        self.__model_plot_filename = persisted_models_dirname + '/' + model_decamelized + "_plot.png"

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
        self.__inputs_scaler = self._load_object(self.__inputs_scaler_filename)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_object(self.__model, self.__model_filename)
        self._save_object(self.__inputs_scaler, self.__inputs_scaler_filename)
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
          self._preprocess_inputs(dataset.iloc[:, 2:-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1/4,
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
        }

    def __plot(self):
        X1, X2 = np.meshgrid(
            np.arange(
                start = self.__inputs_test[:, 0].min() - 10,
                stop = self.__inputs_test[:, 0].max() + 10,
                step = 0.25
            ),
            np.arange(
                start = self.__inputs_test[:, 1].min() - 1000,
                stop = self.__inputs_test[:, 1].max() + 1000,
                step = 0.25
            )
        )

        print('Transforming inputs')
        transformed_inputs = self._transform_input_features(np.array([X1.ravel(), X2.ravel()]).T)
        
        print('Plotting grid predictions')
        plt.contourf(
            X1,
            X2,
            self.__model.predict(transformed_inputs).reshape(X1.shape),
            alpha = 0.5,
            cmap = ListedColormap(('red', 'blue')),
        )
        plt.xlim(X1.min(), X1.max())
        plt.ylim(X2.min(), X2.max())

        print('Plotting samples predictions')
        for i, j in enumerate(np.unique(self.__outputs_test)):
            plt.scatter(
                self.__inputs_test[self.__outputs_test == j, 0],
                self.__inputs_test[self.__outputs_test == j, 1],
                c = ListedColormap(('red', 'blue'))(i),
                label = j,
            )
    
        plt.title(self.model_name + ' (Training set)')
        plt.xlabel('Age')
        plt.ylabel('Estimated salary')
        plt.legend()

        print('Saving figure')
        plt.savefig(dirname + '/' + self.__model_plot_filename)
        plt.clf()