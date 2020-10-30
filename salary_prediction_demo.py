from models.salary_prediction.model import SalaryPredictionModel

model = SalaryPredictionModel()
evaluation = model.train()

print(evaluation)

model.save()
y_pred = model.predict([[1.4]])

model2 = SalaryPredictionModel()
model2.load()
y_pred2 = model2.predict([[1.4]])

print(y_pred)
print(y_pred2)