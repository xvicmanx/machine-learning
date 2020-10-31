from linear_regression_model import LinearRegressionSalaryPredictionModel
from polynomial_regression_model import PolynomialRegressionSalaryPredictionModel
from decision_tree_regression_model import DecisionTreeRegressionSalaryPredictionModel

print('Training salary prediction models: Start')

linear_model = LinearRegressionSalaryPredictionModel()
poly_reg_model = PolynomialRegressionSalaryPredictionModel()
decision_tree_model = DecisionTreeRegressionSalaryPredictionModel()
evaluation = {
  'Linear Model': linear_model.train(),
  'Polynomial Model': poly_reg_model.train(),
  'Decision Tree Model': decision_tree_model.train(),
}

print('Training salary prediction models: End')

print('\tTraining evalutation results')

for key in evaluation:
    print('\t' + key + ' R2 Score = ' + evaluation[key]['r2_score'])

print('\nSaving models')

linear_model.save()
poly_reg_model.save()
decision_tree_model.save()
