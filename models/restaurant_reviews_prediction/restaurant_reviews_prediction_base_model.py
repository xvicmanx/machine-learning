import os.path
import decamelize
import numpy as np
import pandas as pd
import joblib
import nltk
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, fbeta_score
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'


class RestaurantReviewsPredictionModel:
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.tsv'

    __negative_words_contractions = {
        'isn\'t': 'is not',
        'aren\'t': 'are not',
        'wasn\'t': 'was not',
        'weren\'t': 'were not',
        'can\'t': 'cannot',
        'couldn\'t': 'could not',
        'mustn\'t': 'must not',
        'shouldn\'t': 'should not',
        'don\'t': 'do not',
        'doesn\'t': 'does not',
        'didn\'t': 'did not',
        'haven\'t': 'have not',
        'hasn\'t': 'has not',
        'hadn\'t': 'had not',
        'won\'t': 'will not',
        'wouldn\'t': 'would not',
    }

    def __init__(self):
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__
        self.__vectorizer = None
        model_decamelized = decamelize.convert(self.model_name)

        self.__model_filename = persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
        self.__vectorizer_filename = persisted_models_dirname + '/' + model_decamelized + "_vectorizer.sav"
        self.__model_plot_filename = persisted_models_dirname + '/' + model_decamelized + "_plot.png"
        self.__stemmer = PorterStemmer()

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
        self.__vectorizer = self._load_object(self.__vectorizer_filename)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_object(self.__model, self.__model_filename)
        self._save_object(self.__vectorizer, self.__vectorizer_filename)

    def _save_object(self, obj, filename):
        joblib.dump(obj, dirname + '/' + filename)
    
    def _load_object(self, filename):
        return joblib.load(dirname + '/' + filename)

    def _get_model_instance(self):
        raise Exception('Method not implemented')

    def _preprocess_inputs(self, inputs):
        items = []
        for row in inputs:
            items.append(self.__preprocess_text(row[0]))

        # Generate bag of words
        if self.__vectorizer is None:
            self.__vectorizer = CountVectorizer(max_features = 1500)
            return self.__vectorizer.fit_transform(items).toarray()

        return self.__vectorizer.transform(items).toarray()

    def __preprocess_text(self, text):
        # Lowercase text
        text = text.lower()
        negative_words = self.__negative_words_contractions
        # Replace negative words contraction by two words
        for word in negative_words:
            text = re.sub(word, negative_words[word], text)
        
        # Removing not alphabetic characters
        text = re.sub('[^a-z]', ' ', text)

        text = re.sub('not ([a-z]+)', r'not_\1', text)

        # Remove stop words that are not negative
        # TODO
    
        # Apply stemming
        tokens = text.split()
        tokens = [self.__stemmer.stem(token) for token in tokens]

        return ' '.join(tokens)

    def _preprocess_outputs(self, outputs):
        return outputs

    def _transform_input_features(self, inputs):
        return inputs
    
    def _transform_outputs(self, outputs):
        return outputs

    def _inverse_transform_outputs(self, transformed_outputs):
        return transformed_outputs

    def __read_and_process_data(self):
        dataset = pd.read_csv(
            dirname + '/' + self.__dataset_filename,
            delimiter = '\t',
            quoting = 3,
        )
        inputs_train, inputs_test, outputs_train, outputs_test = train_test_split(
          self._preprocess_inputs(dataset.iloc[:, :-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1/5,
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