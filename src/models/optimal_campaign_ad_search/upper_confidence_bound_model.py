import math

import optimal_campaign_ad_search_base_model as base_model


class UpperConfidenceBoundOptAdSearchModel(base_model.OptAdSearchBaseModel):
    def __init__(self):
        super().__init__()
        self.__sum_of_rewards = [0] * self._number_of_options

    """Finds the optimal option to take
    """
    def optimal_option(self):
        self._increase_round_count()
        max_ucb = 0
        selected_option = 0

        for option in range(0, self._number_of_options):
            ucb = self.__upper_confidence_bound(option)
            if ucb > max_ucb:
                max_ucb = ucb
                selected_option = option

        return selected_option

    """Loads the serialized model
    """
    def load(self):
        data = self._load_object(self._model_filename)
        self.__sum_of_rewards = data['sum_of_rewards']
        self._number_of_times_selected = data['number_of_times_selected']
        self._round_count = data['round_count']


    """Save a serialized version of the model to a file
    """
    def save(self):
        data = {
            'sum_of_rewards': self.__sum_of_rewards,
            'number_of_times_selected': self._number_of_times_selected,
            'round_count': self._round_count,
        }
        self._save_object(data, self._model_filename)
        self._plot()

    def _update_option_reward(self, option, reward):
        self.__sum_of_rewards[option] = self.__sum_of_rewards[option] + reward 

    def __upper_confidence_bound(self, option):
        if self._number_of_times_selected[option] > 0:
            return self.__average_reward(option) + self.__confidence_interval_delta(option)
        # A big value to make sure options that has not been selected
        # get selected
        return 10000000000000

    def __confidence_interval_delta(self, option):
        numerator = 3 * math.log(self._round_count)
        denominator = 2 * self._number_of_times_selected[option]
        return math.sqrt(numerator / denominator)

    def __average_reward(self, option):
        return self.__sum_of_rewards[option] / self._number_of_times_selected[option]