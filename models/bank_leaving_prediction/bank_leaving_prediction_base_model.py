import os.path
import decamelize
import pandas as pd

from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from core.classification_model import ClassificationModel

dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class BankLeavingPredictionModel(ClassificationModel):
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.csv'

    def __init__(self):
        super().__init__()

        base = dirname + '/' + persisted_models_dirname + '/' + decamelize.convert(self.__class__.__name__)
        
        self.__inputs_scaler = None
        self.__inputs_label_encoder = None
        self.__inputs_one_hot_encoder = None
        self.__model_file_path = base + "_serialized.sav"
        self.__inputs_scaler_file_path = base + '_inputs_scaler.sav'
        self.__inputs_label_encoder_file_path = base + '_label_encoder.sav'
        self.__inputs_one_hot_encoder_file_path = base + '_one_hot_encoder.sav'


    def load(self):
        """Loads the serialized model
        """
        self._load_model(self.__model_file_path)
        self.__inputs_scaler = self._load_object(self.__inputs_scaler_file_path)
        self.__inputs_label_encoder = self._load_object(self.__inputs_label_encoder_file_path)
        self.__inputs_one_hot_encoder = self._load_object(self.__inputs_one_hot_encoder_file_path)

    def save(self):
        """Save a serialized version of the model to a file
        """
        self._save_model(self.__model_file_path)
        self._save_object(self.__inputs_scaler, self.__inputs_scaler_file_path)
        self._save_object(self.__inputs_label_encoder, self.__inputs_label_encoder_file_path)
        self._save_object(self.__inputs_one_hot_encoder, self.__inputs_one_hot_encoder_file_path)

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

    def _transform_inputs(self, inputs):
        if self.__inputs_scaler is None:
            self.__inputs_scaler = StandardScaler()
            return self.__inputs_scaler.fit_transform(inputs)

        return self.__inputs_scaler.transform(inputs)
    
    def _split_data(self):
        dataset = pd.read_csv(dirname + '/' + self.__dataset_filename)
        train_inputs, test_inputs, train_outputs, test_outputs = train_test_split(
          self._preprocess_inputs(dataset.iloc[:, 3:-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1 / 5,
          random_state = 0,
          stratify = dataset.iloc[:, -1].values,
        )
        return train_inputs, train_outputs, test_inputs, test_outputs
