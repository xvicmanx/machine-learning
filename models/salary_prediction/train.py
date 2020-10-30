from model import SalaryPredictionModel

print('Training Salary Prediction Model: Start')
model = SalaryPredictionModel()
evaluation = model.train()
print('Training Salary Prediction Model: End')

print('\tTraining Evalutation Results')
print('\tR2 Score = ' + evaluation['r2_score'])

print('Saving Model')
model.save()
