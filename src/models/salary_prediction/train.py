import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from helpers import  train_and_evaluate, display_predictions, display_regression_evaluation

from linear_regression_model import LinearRegressionSalaryPredictionModel
from polynomial_regression_model import PolynomialRegressionSalaryPredictionModel
from decision_tree_regression_model import DecisionTreeRegressionSalaryPredictionModel
from random_forest_regression_model import RandomForestRegressionSalaryPredictionModel
from support_vector_regression_model import SupportVectorRegressionSalaryPredictionModel

title = 'Training salary prediction models'

print(title + ': Start')

models = {
    'Linear Model': LinearRegressionSalaryPredictionModel(),
    'Polynomial Model': PolynomialRegressionSalaryPredictionModel(),
    'Decision Tree Model': DecisionTreeRegressionSalaryPredictionModel(),
    'Random Forest Model': RandomForestRegressionSalaryPredictionModel(),
    'Support Vector Regression Model': SupportVectorRegressionSalaryPredictionModel(),
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_regression_evaluation(evaluation)
display_predictions(models, [[1.4]])

print('\nSaving models')


for key in models:
   models[key].save()