from linear_regression_model import LinearRegressionSalaryPredictionModel
from polynomial_regression_model import PolynomialRegressionSalaryPredictionModel
from decision_tree_regression_model import DecisionTreeRegressionSalaryPredictionModel
from random_forest_regression_model import RandomForestRegressionSalaryPredictionModel

print('Training salary prediction models: Start')

linear_model = LinearRegressionSalaryPredictionModel()
poly_reg_model = PolynomialRegressionSalaryPredictionModel()
decision_tree_model = DecisionTreeRegressionSalaryPredictionModel()
random_forest_model = RandomForestRegressionSalaryPredictionModel()

evaluation = {
  'Linear Model': linear_model.train(),
  'Polynomial Model': poly_reg_model.train(),
  'Decision Tree Model': decision_tree_model.train(),
  'Random Forest Model': random_forest_model.train(),
}

print('Training salary prediction models: End')

print('\tTraining evalutation results')

for key in evaluation:
    print('\t' + key + ' R2 Score = ' + evaluation[key]['r2_score'])

print('\nSaving models')

linear_model.save()
poly_reg_model.save()
decision_tree_model.save()
random_forest_model.save()
