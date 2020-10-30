from models.salary_prediction.linear_regression_model import LinearRegressionSalaryPredictionModel

model = LinearRegressionSalaryPredictionModel()
evaluation = model.train()

print(evaluation)

model.save()
y_pred = model.predict([[1.4]])

model2 = LinearRegressionSalaryPredictionModel()
model2.load()
y_pred2 = model2.predict([[1.4]])

print(y_pred)
print(y_pred2)