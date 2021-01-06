
import tensorflow as tf

import movie_rate_prediction_base_model as bm

class SAENeuralNetwork:
    def __init__(self, outputs):
        self.__model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(units = 20, activation = 'sigmoid'),
            tf.keras.layers.Dense(units = 10, activation = 'sigmoid'),
            tf.keras.layers.Dense(units = 20, activation = 'sigmoid'),
            tf.keras.layers.Dense(units = outputs, activation = 'relu'),
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        self.__model.compile(
            loss = 'mse',
            optimizer = optimizer,
            metrics = [ 'mae', 'mse' ],
        )

    def fit(self, X, y):
        self.__model.fit(x = X, y = y, epochs = 50)

    def predict(self, inputs):
        return self.__model.predict(inputs)

    def save(self, file_path):
        return self.__model.save_weights(file_path)

    def load(self, file_path):
        return self.__model.load_weights(file_path)


class NeuralNetworkModel(bm.MovieRatePredictionModel):
    def __init__(self):
        super().__init__()
        self._model = SAENeuralNetwork(1682)

    def _get_model_instance(self):
        return self._model

    def _save_model(self, file_path):
        self._model.save(file_path)

    def _load_model(self, file_path):
        return self._model.load(file_path)