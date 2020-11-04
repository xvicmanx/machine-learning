from tabulate import tabulate

def display_predictions(models, samples):
    print('\tPredictions')
    prediction_headers = ['Model', 'Prediction']
    prediction_rows = []

    for key in models:
        prediction = models[key].predict(samples)
        prediction_rows.append([key, str(prediction)])

    print(tabulate(
        prediction_rows,
        headers=prediction_headers
    ))

def display_classification_evaluation(evaluation):
    print('\tTraining evaluation results')

    headers = ['Model', 'Accuracy', 'Confusion matrix']
    rows = []

    for key in evaluation:
        rows.append([key, evaluation[key]['accuracy_score'], str(evaluation[key]['confusion_matrix'])])

    print(tabulate(
        rows,
        headers=headers
    ))

def display_regression_evaluation(evaluation):
    print('\tTraining evaluation results')

    headers = ['Model', 'R2 score']
    rows = []

    for key in evaluation:
        rows.append([key, evaluation[key]['r2_score']])

    print(tabulate(
        rows,
        headers=headers
    ))

def train_and_evaluate(models):
    evaluation = {}
    for key in models:
        evaluation[key] = models[key].train()
    
    return evaluation
