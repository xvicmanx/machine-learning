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

print('Training salary prediction models: End')

print('\tTraining evalutation results')

for key in evaluation:
    print('\t' + key + ' R2 Score = ' + evaluation[key]['r2_score'])

# headers = ['Model', 'Accuracy', 'Confusion matrix']
# rows = []

# for key in evaluation:
#     rows.append([key, evaluation[key]['accuracy_score'], str(evaluation[key]['confusion_matrix'])])

# print(tabulate(
#     rows,
#     headers=headers
# ))

print('\nSalary prediction (Linear model) for' + ' 1.4 years = ' + str(linear_model.predict([[1.4]])))
print('Salary prediction (Polynomial model) for' + ' 1.4 years = ' + str(poly_reg_model.predict([[1.4]])))
print('Salary prediction (Decision tree model) for' + ' 1.4 years = ' + str(decision_tree_model.predict([[1.4]])))
print('Salary prediction (Random forest model) for' + ' 1.4 years = ' + str(random_forest_model.predict([[1.4]])))
print('Salary prediction (SVR model) for' + ' 1.4 years = ' + str(svr_model.predict([[1.4]])))

print('\nSaving models')


linear_model.save()
poly_reg_model.save()
decision_tree_model.save()
random_forest_model.save()
svr_model.save()