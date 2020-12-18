import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from helpers import train_and_evaluate, display_predictions, display_classification_evaluation

from svm_classification_model import SupportVectorMachinesBankLeavingPredictionModel
from random_forest_classification_model import RandomForestBankLeavingPredictionModel
from neural_network_classification_model import NeuralNetworkBankLeavingPredictionModel
from neural_network_v2_classification_model import NeuralNetworkV2BankLeavingPredictionModel

title = 'Training bank leaving prediction models'

print(title + ': Start')

models = {
    'SVM Model': SupportVectorMachinesBankLeavingPredictionModel(),
    'Random Forest Model': RandomForestBankLeavingPredictionModel(),
    'Neural Network Model': NeuralNetworkBankLeavingPredictionModel(),
    'Neural Network V2 Model': NeuralNetworkV2BankLeavingPredictionModel()
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_classification_evaluation(evaluation)
display_predictions(models, [[502, 'France', 'Female', 42, 8, 159660.8, 3, 1, 0, 113931.57]])

print('\nSaving models')


for key in models:
   models[key].save()
