
import tensorflow as tf
import os.path

import bank_leaving_prediction_base_model as bm

class NeuralNetwork:
    def __init__(self):
        self.__model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(6, activation = 'relu'),
            tf.keras.layers.Dense(6, activation = 'relu'),
            tf.keras.layers.Dense(1, activation = 'sigmoid')
        ])

        self.__model.compile(
            optimizer = 'adam',
            loss = 'binary_crossentropy',
            metrics = ['accuracy']
        )

    def fit(self, X, y):
        self.__model.fit(X, y, epochs = 100, batch_size = 32)

    def predict(self, input):
        return self.__model.predict(input).round()

    def save(self, filename):
        return self.__model.save_weights(filename)

    def load(self, filename):
        return self.__model.load_weights(filename)


dirname = os.path.dirname(__file__)

class NeuralNetworkV2BankLeavingPredictionModel(bm.BankLeavingPredictionModel):
    def __init__(self):
        super().__init__()
        self.__model = NeuralNetwork()

    def _get_model_instance(self):
        return self.__model

    def _save_model(self, filename):
        self.__model.save(dirname + '/' + filename)

    def _load_model(self, filename):
        return self.__model.load(dirname + '/' + filename)