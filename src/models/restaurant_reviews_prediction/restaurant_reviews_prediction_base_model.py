import os.path
import decamelize
import numpy as np
import pandas as pd
import joblib
import nltk
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer

from core.classification_model import ClassificationModel

dirname = os.path.dirname(__file__)
persisted_models_dirname = 'persisted_models_data'

class RestaurantReviewsPredictionModel(ClassificationModel):
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.tsv'

    __stop_words = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"])

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
        super().__init__()

        base = dirname + '/' + persisted_models_dirname + '/' + decamelize.convert(self.__class__.__name__)

        self.__vectorizer = None
        self.__model_file_path = base + "_serialized.sav"
        self.__vectorizer_file_path = base + "_vectorizer.sav"
        self.__model_plot_file_path = base + "_plot.png"
        self.__stemmer = PorterStemmer()

    """Loads the serialized model
    """
    def load(self):
        self._load_model(self.__model_file_path)
        self.__vectorizer = self._load_object(self.__vectorizer_file_path)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_model(self.__model_file_path)
        self._save_object(self.__vectorizer, self.__vectorizer_file_path)

    def _preprocess_inputs(self, inputs):
        items = []
        for row in inputs:
            items.append(self.__preprocess_text(row[0]))

        return np.array(items)

    def _transform_inputs(self, inputs):
        # Generate bag of words
        if self.__vectorizer is None:
            self.__vectorizer = CountVectorizer(max_features = 1500)
            return self.__vectorizer.fit_transform(inputs).toarray()

        return self.__vectorizer.transform(inputs).toarray()

    def _split_data(self):
        dataset = pd.read_csv(
            dirname + '/' + self.__dataset_filename,
            delimiter = '\t',
            quoting = 3,
        )
        train_inputs, test_inputs, train_outputs, test_outputs = train_test_split(
          self._preprocess_inputs(dataset.iloc[:, :-1].values),
          self._preprocess_outputs(dataset.iloc[:, -1].values),
          test_size = 1/5,
          random_state = 0,
        )
        return train_inputs, train_outputs, test_inputs, test_outputs

    def __preprocess_text(self, text):
        # Lowercase text
        text = text.lower()
        negative_words = self.__negative_words_contractions
        # Replace negative words contraction by two words
        for word in negative_words:
            text = re.sub(word, negative_words[word], text)
        
        # Removing not alphabetic characters
        text = re.sub('[^a-z]', ' ', text)
    
        # Apply stemming
        tokens = text.split()
        
        # Remove stop words that are not negative
        tokens = [word for word in tokens if word not in self.__stop_words]

        tokens = [self.__stemmer.stem(token) for token in tokens]

        return ' '.join(tokens)