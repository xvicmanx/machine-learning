from linear_regression_model import LinearRegressionSalaryPredictionModel
from polynomial_regression_model import PolynomialRegressionSalaryPredictionModel

print('Training salary prediction models: Start')

linear_model = LinearRegressionSalaryPredictionModel()
poly_reg_model = PolynomialRegressionSalaryPredictionModel()
evaluation = {
  'Linear Model': linear_model.train(),
  'Polynomial Model': poly_reg_model.train(),
}

print('Training salary prediction models: End')

print('\tTraining evalutation results')

for key in evaluation:
    print('\t' + key + ' R2 Score = ' + evaluation[key]['r2_score'])

print('\nSaving models')

linear_model.save()
poly_reg_model.save()
