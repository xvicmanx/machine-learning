import math
import pandas as pd
import os.path
import joblib
import matplotlib.pyplot as plt
import numpy as np
import decamelize


dirname = os.path.dirname(__file__)

class OptAdSearchBaseModel:
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.csv'
    _persisted_models_dirname = 'persisted_models_data'

    def __init__(self):
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__
        
        model_decamelized = decamelize.convert(self.model_name)

        self._number_of_options = 10
        self._number_of_times_selected = [0] * self._number_of_options
        self._round_count = 0
        self._model_filename = self._persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
        self.__model_plot_filename = self._persisted_models_dirname + '/' + model_decamelized + "_plot.png"

 
    """Trains the model with initial data
    """
    def train(self, total_of_rounds = 10000):
        dataset = pd.read_csv(dirname + '/' + self.__dataset_filename)
        items = dataset.values
    
        for n in range(0, total_of_rounds):
            option = self.optimal_option()
            reward = items[n, option]
            self.add_option_reward(option, reward)


    """Add a reward to a taken option
    """
    def add_option_reward(self, option, reward):
        self.__increase_selections_count(option)
        self._update_option_reward(option, reward)

    """Finds the optimal option to take
    """
    def optimal_option(self):
        raise Exception('Method not implemented')

    """Loads the serialized model
    """
    def load(self):
        raise Exception('Method not implemented')

    """Save a serialized version of the model to a file
    """
    def save(self):
        raise Exception('Method not implemented')

    def _update_option_reward(self, option, reward):
        raise Exception('Method not implemented')

    def _save_object(self, obj, filename):
        joblib.dump(obj, dirname + '/' + filename)
    
    def _load_object(self, filename):
        return joblib.load(dirname + '/' + filename)

    def __increase_selections_count(self, option):
        self._number_of_times_selected[option] = self._number_of_times_selected[option] + 1

    def _increase_round_count(self):
        self._round_count = self._round_count + 1


    def _plot(self):
        plt.title('Optimal campaign Ad selection (' + self.model_name + ')')
        plt.xlabel('Ad')
        plt.ylabel('Selections')

        options =  ['Ad ' + str(i + 1) for i in range(0, self._number_of_options)]
        positions = np.arange(len(options))
        plt.bar(positions, self._number_of_times_selected, align='center', alpha=0.5)
        plt.xticks(positions, options)

        plt.savefig(dirname + '/' + self.__model_plot_filename)
        plt.clf()