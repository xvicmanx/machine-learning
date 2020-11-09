import math
import pandas as pd
import os.path
import joblib
import matplotlib.pyplot as plt
import numpy as np
import decamelize


dirname = os.path.dirname(__file__)

class UpperConfidenceBoundOptAdSearchModel:
    # File of the dataset used to train the model
    __dataset_filename = 'dataset.csv'
    _persisted_models_dirname = 'persisted_models_data'

    def __init__(self):
        super().__init__()
        # File to stored the serialized version of the model
        self.model_name = self.__class__.__name__
        
        model_decamelized = decamelize.convert(self.model_name)

        self.__number_of_options = 10
        self.__sum_of_rewards = [0] * self.__number_of_options
        self.__number_of_times_selected = [0] * self.__number_of_options
        self.__round_count = 0
        self.__model_filename = self._persisted_models_dirname + '/' + model_decamelized + "_serialized.sav"
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
        self.__number_of_times_selected[option] = self.__number_of_times_selected[option] + 1
        self.__sum_of_rewards[option] = self.__sum_of_rewards[option] + reward 

    """Finds the optimal option to take
    """
    def optimal_option(self):
        max_ucb = 0
        selected_option = 0
        self.__round_count = self.__round_count + 1

        for option in range(0, self.__number_of_options):
            ucb = self.__upper_confidence_bound(option)
            if ucb > max_ucb:
                max_ucb = ucb
                selected_option = option

        return selected_option

    """Loads the serialized model
    """
    def load(self):
        data = self._load_object(self.__model_filename)
        self.__sum_of_rewards = data['sum_of_rewards']
        self.__number_of_times_selected = data['number_of_times_selected']
        self.__round_count = data['round_count']


    """Save a serialized version of the model to a file
    """
    def save(self):
        data = {
            'sum_of_rewards': self.__sum_of_rewards,
            'number_of_times_selected': self.__number_of_times_selected,
            'round_count': self.__round_count,
        }
        self._save_object(data, self.__model_filename)
        self.__plot()

    def _save_object(self, obj, filename):
        joblib.dump(obj, dirname + '/' + filename)
    
    def _load_object(self, filename):
        return joblib.load(dirname + '/' + filename)

    def __plot(self):
        plt.title('Optimal campaign Ad selection')
        plt.xlabel('Ad')
        plt.ylabel('Selections')

        options =  ['Ad ' + str(i + 1) for i in range(0, self.__number_of_options)]
        positions = np.arange(len(options))
        plt.bar(positions, self.__number_of_times_selected, align='center', alpha=0.5)
        plt.xticks(positions, options)

        plt.savefig(dirname + '/' + self.__model_plot_filename)
        plt.clf()

    def __upper_confidence_bound(self, option):
        if self.__number_of_times_selected[option] > 0:
            return self.__average_reward(option) + self.__confidence_interval_delta(option)
        # A big value to make sure options that has not been selected
        # get selected
        return 10000000000000

    def __confidence_interval_delta(self, option):
        numerator = 3 * math.log(self.__round_count)
        denominator = 2 * self.__number_of_times_selected[option]
        return math.sqrt(numerator / denominator)

    def __average_reward(self, option):
        return self.__sum_of_rewards[option] / self.__number_of_times_selected[option]