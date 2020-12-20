import numpy as np
import pandas as pd
import joblib
import os.path
import decamelize
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)

class KMeansClusteringModel:
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.csv'
    _persisted_models_dirname = 'persisted_models_data/k_means'

    def __init__(self, number_of_clusters = 5):
        self.__number_of_clusters = number_of_clusters
        
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__ + '_' + str(number_of_clusters) + 'Clusters'
        
        model_decamelized = decamelize.convert(self.model_name)

        self.__model_filename = self._persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
        self.__model_plot_filename = self._persisted_models_dirname + '/' + model_decamelized + "_plot.png"

    """Trains the model by reading the data from file, preprocessing and training the model
    """
    def train(self):
        self.__read_and_process_data()
        self.__model = self._get_model_instance()
        self.__model.fit(self.__inputs)
        return self.__evaluate()

    """Predicts the value of the list of given values
    """
    def predict(self, items):
        return self.__model.predict(items)

    """Loads the serialized model
    """
    def load(self):
        self.__model = self._load_object(self.__model_filename)

    """Save a serialized version of the model to a file
    """
    def save(self):
        self._save_object(self.__model, self.__model_filename)
        self.__plot()

    def centers(self):
        self.__model.cluster_centers_

    def _save_object(self, obj, filename):
        joblib.dump(obj, dirname + '/' + filename)
    
    def _load_object(self, filename):
        return joblib.load(dirname + '/' + filename)

    def _get_model_instance(self):
        return KMeans(
            init = 'k-means++',
            n_clusters = self.__number_of_clusters,
            random_state = 0
        ).fit(self.__inputs)

    def __evaluate(self):
        return {
            # Sum of squared distances of samples to their closest cluster center.
            # within cluster sum of squares (WCSS)
            'wcss': self.__model.inertia_,
        }

    def __read_and_process_data(self):
        dataset = pd.read_csv(dirname + '/' + self.__dataset_filename)
        self.__inputs = dataset.iloc[:, [3, 4]].values

    def __plot(self):
        predictions = self.__model.predict(self.__inputs)
        colors = [
            'tab:blue',
            'tab:orange',
            'tab:green',
            'tab:red',
            'tab:purple',
            'tab:brown',
            'tab:pink',
            'tab:gray',
            'tab:olive',
            'tab:cyan',
        ]

        plt.title('K-Means ' + str(self.__number_of_clusters) + ' Clusters assignments')

        for i in range(0, self.__number_of_clusters):
            filtered_inputs = self.__inputs[predictions == i, :]
            plt.scatter(
                filtered_inputs[:, 0],
                filtered_inputs[:, 1],
                s = 30,
                c = colors[i],
                label = 'Cluster ' + str(i + 1),
            )

        plt.scatter(
            self.__model.cluster_centers_[:, 0],
            self.__model.cluster_centers_[:, 1],
            s = 60,
            c = 'black',
            label = 'Centroids',
        )
        
        plt.xlabel('Annual Income')
        plt.ylabel('Spending Score')
        plt.legend()
        plt.savefig(dirname + '/' + self.__model_plot_filename)
        plt.clf()