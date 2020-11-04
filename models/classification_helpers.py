from tabulate import tabulate

def tabulate_predictions(models, samples):
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
