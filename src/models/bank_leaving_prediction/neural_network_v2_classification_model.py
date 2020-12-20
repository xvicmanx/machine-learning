
import tensorflow as tf

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

    def save(self, file_path):
        return self.__model.save_weights(file_path)

    def load(self, file_path):
        return self.__model.load_weights(file_path)


class NeuralNetworkV2BankLeavingPredictionModel(bm.BankLeavingPredictionModel):
    def __init__(self):
        super().__init__()
        self._model = NeuralNetwork()

    def _get_model_instance(self):
        return self._model

    def _save_model(self, file_path):
        self._model.save(file_path)

    def _load_model(self, file_path):
        return self._model.load(file_path)