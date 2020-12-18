import os.path
import decamelize
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from core.classification_model import ClassificationModel

dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class CatOrDogPredictionModel(ClassificationModel):
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
        train_generator = ImageDataGenerator(
            rescale = 1./255,
            shear_range = 0.2,
            zoom_range = 0.2,
            horizontal_flip = True,
        )

        test_generator = ImageDataGenerator(rescale = 1./255)
        
        test_set = test_generator.flow_from_directory(
            dirname  + '/datasets/test',
            target_size = (64, 64),
            batch_size = 5001,
            class_mode = 'binary',
        )

        train_set = train_generator.flow_from_directory(
            dirname  + '/datasets/train',
            target_size = (64, 64),
            batch_size = 32,
            class_mode = 'binary',
        )

        test_inputs = []
        test_outputs = []
        test_set.reset()

        for _ in range(test_set.__len__()):
            a, b = test_set.next()
            test_inputs.append(a)
            test_outputs.append(b)
        
        test_inputs = np.array(test_inputs)
        test_outputs = np.array(test_outputs)

        return train_set, None, test_inputs, test_outputs
