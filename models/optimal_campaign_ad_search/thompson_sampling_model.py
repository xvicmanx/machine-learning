import random

import optimal_campaign_ad_search_base_model as base_model


class ThompsonSamplingOptAdSearchModel(base_model.OptAdSearchBaseModel):
    def __init__(self):
        super().__init__()
        self.__rewards_counts = [
            [0] * self._number_of_options,
            [0] * self._number_of_options,
        ]

    """Finds the optimal option to take
    """
    def optimal_option(self):
        self._increase_round_count()
        max_random = 0
        selected_option = 0

        for option in range(0, self._number_of_options):
            random_beta = self.__random_beta(option)
            if random_beta > max_random:
                max_random = random_beta
                selected_option = option

        return selected_option

    """Loads the serialized model
    """
    def load(self):
        data = self._load_object(self._model_filename)
        self.__rewards_counts = data['rewards_counts']
        self._number_of_times_selected = data['number_of_times_selected']
        self._round_count = data['round_count']


    """Save a serialized version of the model to a file
    """
    def save(self):
        data = {
            'rewards_counts': self.__rewards_counts,
            'number_of_times_selected': self._number_of_times_selected,
            'round_count': self._round_count,
        }
        self._save_object(data, self._model_filename)
        self._plot()

    def _update_option_reward(self, option, reward):
        self.__rewards_counts[reward][option] = self.__rewards_counts[reward][option] + 1

    def __random_beta(self, option):
        return random.betavariate(
            self.__rewards_counts[1][option] + 1,
            self.__rewards_counts[0][option] + 1,
        )