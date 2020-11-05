import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from helpers import  train_and_evaluate, display_predictions, display_classification_evaluation

from k_nearest_neighbor_classification_model import KNearestNeighborSocialNetworkAdsPredictionModel
from decision_tree_classification_model import DecisionTreeSocialNetworkAdsPredictionModel
from naive_bayes_classification_model import NaiveBayesSocialNetworkAdsPredictionModel
from logistic_regression_classification_model import LogisticRegressionSocialNetworkAdsPredictionModel
from svm_classification_model import SupportVectorMachinesSocialNetworkAdsPredictionModel
from random_forest_classification_model import RandomForestSocialNetworkAdsPredictionModel


title = 'Training social network ads prediction models'

print(title + ': Start')

models = {
    'K Nearest Neighbors Model': KNearestNeighborSocialNetworkAdsPredictionModel(),
    'Decision Tree Model': DecisionTreeSocialNetworkAdsPredictionModel(),
    'Naive Bayes Model': NaiveBayesSocialNetworkAdsPredictionModel(),
    'Logistic Regression Model': LogisticRegressionSocialNetworkAdsPredictionModel(),
    'SVM Model': SupportVectorMachinesSocialNetworkAdsPredictionModel(),
    'Random Forest Model': RandomForestSocialNetworkAdsPredictionModel(),
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_classification_evaluation(evaluation)
display_predictions(models, [[32, 18000]])

print('\nSaving models')


for key in models:
   models[key].save()
