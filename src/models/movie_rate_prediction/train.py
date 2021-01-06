import os, sys
import numpy as np
from tensorflow.keras.preprocessing import image

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from helpers import train_and_evaluate, display_predictions, display_regression_evaluation

from neural_network_model import NeuralNetworkModel

title = 'Movie rate prediction models'

print(title + ': Start')

models = {
    'Neural Network Model': NeuralNetworkModel()
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_regression_evaluation(evaluation)

print('\nSaving models')


for key in models:
   models[key].save()
