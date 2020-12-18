
import tensorflow as tf

import cat_or_dog_prediction_base_model as bm

class ConvolutionalNeuralNetwork:
    def __init__(self):
        self.__model = tf.keras.models.Sequential([
            # First Convolution Layer
            tf.keras.layers.Conv2D(
                filters = 32,
                kernel_size = 3,
                activation = 'relu',
                input_shape = [64, 64, 3],
            ),
            tf.keras.layers.MaxPool2D(pool_size = 2, strides = 2),
            
            # Second Convolution Layer 
            tf.keras.layers.Conv2D(
                filters = 32,
                kernel_size = 3,
                activation = 'relu',
            ),
            tf.keras.layers.MaxPool2D(
                pool_size = 2,
                strides = 2,
            ),
            tf.keras.layers.Flatten(),
            # Dense layers
            tf.keras.layers.Dense(units = 128, activation = 'relu'),
            tf.keras.layers.Dense(units = 1, activation = 'sigmoid'),
        ])

        self.__model.compile(
            optimizer = 'adam',
            loss = 'binary_crossentropy',
            metrics = ['accuracy']
        )

    def fit(self, X, y):
        self.__model.fit(x = X, epochs = 25)

    def predict(self, inputs):
        return self.__model.predict(inputs).round()

    def save(self, file_path):
        return self.__model.save_weights(file_path)

    def load(self, file_path):
        return self.__model.load_weights(file_path)


class NeuralNetworkCatOrDogPredictionModel(bm.CatOrDogPredictionModel):
    def __init__(self):
        super().__init__()
        self.__model = ConvolutionalNeuralNetwork()

    def _get_model_instance(self):
        return self.__model

    def _save_model(self, file_path):
        self.__model.save(file_path)

    def _load_model(self, file_path):
        return self.__model.load(file_path)