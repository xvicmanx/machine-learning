from tabulate import tabulate

from k_nearest_neighbor_classification_model import KNearestNeighborSocialNetworkAdsPredictionModel


print('Training social network ads prediction models: Start')

k_neighbors_model = KNearestNeighborSocialNetworkAdsPredictionModel()

evaluation = {
    'K Nearest Neighbors Model': k_neighbors_model.train(),
}

print('Training social network ads prediction models: End')

print('\tTraining evaluation results')

headers = ['Model', 'Accuracy', 'Confusion matrix']
rows = []

for key in evaluation:
    rows.append([key, evaluation[key]['accuracy_score'], str(evaluation[key]['confusion_matrix'])])

print(tabulate(
    rows,
    headers=headers
))

print('\nSalary prediction (K Nearest Neighbors Model) ' + str(k_neighbors_model.predict([[32,18000]])))

print('\nSaving models')


k_neighbors_model.save()