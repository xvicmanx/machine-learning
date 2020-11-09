from upper_confidence_bound_model import UpperConfidenceBoundOptAdSearchModel
from thompson_sampling_model import ThompsonSamplingOptAdSearchModel

title = 'Training optimal campaign ad search models'

print(title + ': Start')

ucb_model = UpperConfidenceBoundOptAdSearchModel()
thompson_model = ThompsonSamplingOptAdSearchModel()

ucb_model.train()
thompson_model.train()

print('\n Saving models')
ucb_model.save()
thompson_model.save()

print('\n Loading models')
ucb_model.load()
thompson_model.load()

ucb_option = ucb_model.optimal_option()
thompson_option = thompson_model.optimal_option()

print('\n Ad selected UCB: ' + str(ucb_option + 1))
print('\n Ad selected Thompson Sampling: ' + str(thompson_option + 1))

ucb_model.add_option_reward(ucb_option , 1)
ucb_model.add_option_reward(thompson_option , 1)

print(title + ': End')