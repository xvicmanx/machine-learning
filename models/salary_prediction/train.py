from tabulate import tabulate

from linear_regression_model import LinearRegressionSalaryPredictionModel
from polynomial_regression_model import PolynomialRegressionSalaryPredictionModel
from decision_tree_regression_model import DecisionTreeRegressionSalaryPredictionModel
from random_forest_regression_model import RandomForestRegressionSalaryPredictionModel
from support_vector_regression_model import SupportVectorRegressionSalaryPredictionModel

print('Training salary prediction models: Start')

linear_model = LinearRegressionSalaryPredictionModel()
poly_reg_model = PolynomialRegressionSalaryPredictionModel()
decision_tree_model = DecisionTreeRegressionSalaryPredictionModel()
random_forest_model = RandomForestRegressionSalaryPredictionModel()
svr_model = SupportVectorRegressionSalaryPredictionModel()

evaluation = {
  'Linear Model': linear_model.train(),
  'Polynomial Model': poly_reg_model.train(),
  'Decision Tree Model': decision_tree_model.train(),
  'Random Forest Model': random_forest_model.train(),
  'Support Vector Regression Model': svr_model.train(),
}

print('Training salary prediction models: End\n')

print('\tTraining evalutation results')

headers = ['Model', 'R2 score']
rows = []

for key in evaluation:
    rows.append([key, evaluation[key]['r2_score']])

print(tabulate(
    rows,
    headers=headers,
))

models = [
  ['Linear model', linear_model],
  ['Polynomial model', poly_reg_model],
  ['Decision tree model', decision_tree_model],
  ['Random forest model', random_forest_model],
  ['SVR model', svr_model],
]
prediction_headers = ['Model', 'Result']
prediciton_rows = []

print('\n\tSalary Prediction')
for item in models:
    result = item[1].predict([[1.4]])
    prediciton_rows.append([item[0], result])

print(tabulate(
    prediciton_rows,
    headers=prediction_headers,
))

print('\nSaving models')


linear_model.save()
poly_reg_model.save()
decision_tree_model.save()
random_forest_model.save()
svr_model.save()