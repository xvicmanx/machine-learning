from k_nearest_neighbor_classification_model import KNearestNeighborSocialNetworkAdsPredictionModel


print('Training social network ads prediction models: Start')

k_neighbors_model = KNearestNeighborSocialNetworkAdsPredictionModel()

evaluation = {
    'K Nearest Neighbors Model': k_neighbors_model.train(),
}

print('Training social network ads prediction models: End')

print('\tTraining evaluation results')
for key in evaluation:
    print('\t' + key + ':')
    print('\t\t' + ' Accuracy score = ' + str(evaluation[key]['accuracy_score']))
    print('\t\t' + ' Confusion Matrix:')
    print('\t\t\t' + str(evaluation[key]['confusion_matrix']))
    print('\n')

print('\nSalary prediction (K Nearest Neighbors Model) ' + str(k_neighbors_model.predict([[32,18000]])))

print('\nSaving models')


k_neighbors_model.save()