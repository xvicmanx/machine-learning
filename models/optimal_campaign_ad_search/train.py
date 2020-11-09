from upper_confidence_bound_model import UpperConfidenceBoundOptAdSearchModel

title = 'Training optimal campaign ad search models'

print(title + ': Start')

ucb_model = UpperConfidenceBoundOptAdSearchModel()

ucb_model.train()

print('\n Saving models')
ucb_model.save()

print('\n Loading models')
ucb_model.load()

option = ucb_model.optimal_option()

print('\n Ad selected ' + str(option + 1))

ucb_model.add_option_reward(option , 1)

print(title + ': End')