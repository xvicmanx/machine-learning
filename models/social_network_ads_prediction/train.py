from tabulate import tabulate

from k_nearest_neighbor_classification_model import KNearestNeighborSocialNetworkAdsPredictionModel
from decision_tree_classification_model import DecisionTreeSocialNetworkAdsPredictionModel


def tabulate_predictions(models):
    print('\tPredictions')
    prediction_headers = ['Model', 'Prediction']
    prediction_rows = []

    for key in models:
        prediction = models[key].predict([[32, 18000]])
        prediction_rows.append([key, str(prediction)])

    print(tabulate(
        prediction_rows,
        headers=prediction_headers
    ))

def tabulate_models_evaluation(evaluation):
    print('\tTraining evaluation results')

    headers = ['Model', 'Accuracy', 'Confusion matrix']
    rows = []

    for key in evaluation:
        rows.append([key, evaluation[key]['accuracy_score'], str(evaluation[key]['confusion_matrix'])])

    print(tabulate(
        rows,
        headers=headers
    ))

def train_and_evaluate(models):
    evaluation = {}
    for key in models:
        evaluation[key] = models[key].train()
    return evaluation


title = 'Training social network ads prediction models'

print(title + ': Start')

models = {
    'K Nearest Neighbors Model': KNearestNeighborSocialNetworkAdsPredictionModel(),
    'Decision Tree Model': DecisionTreeSocialNetworkAdsPredictionModel(),
}

evaluation = train_and_evaluate(models)

print(title + ': End')

tabulate_models_evaluation(evaluation)
tabulate_predictions(models)

print('\nSaving models')


for key in models:
   models[key].save()
