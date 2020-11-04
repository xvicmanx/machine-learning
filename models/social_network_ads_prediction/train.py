import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from classification_helpers import  train_and_evaluate, tabulate_predictions, tabulate_models_evaluation

from k_nearest_neighbor_classification_model import KNearestNeighborSocialNetworkAdsPredictionModel
from decision_tree_classification_model import DecisionTreeSocialNetworkAdsPredictionModel
from naive_bayes_classification_model import NaiveBayesSocialNetworkAdsPredictionModel

title = 'Training social network ads prediction models'

print(title + ': Start')

models = {
    'K Nearest Neighbors Model': KNearestNeighborSocialNetworkAdsPredictionModel(),
    'Decision Tree Model': DecisionTreeSocialNetworkAdsPredictionModel(),
    'Naive Bayes Model': NaiveBayesSocialNetworkAdsPredictionModel(),
}

evaluation = train_and_evaluate(models)

print(title + ': End')

tabulate_models_evaluation(evaluation)
tabulate_predictions(models, [[32, 18000]])

print('\nSaving models')


for key in models:
   models[key].save()
