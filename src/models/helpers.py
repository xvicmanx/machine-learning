from tabulate import tabulate
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def display_predictions(models, samples, to_data_frame = True):
    print('\tPredictions')
    prediction_headers = ['Model', 'Prediction']
    prediction_rows = []

    for key in models:
        prediction = models[key].predict(samples, to_data_frame)
        prediction_rows.append([key, str(prediction)])

    print(tabulate(
        prediction_rows,
        headers=prediction_headers
    ))

def display_classification_evaluation(evaluation):
    print('\tTraining evaluation results')

    headers = ['Model', 'Accuracy', 'F0.5 score', 'F1 score', 'F2 score', 'Confusion matrix']
    rows = []

    for key in evaluation:
        rows.append([
            key,
            evaluation[key]['accuracy_score'],
            evaluation[key]['f0.5_score'],
            evaluation[key]['f1_score'],
            evaluation[key]['f2_score'],
            str(evaluation[key]['confusion_matrix']),
        ])

    print(tabulate(
        rows,
        headers=headers
    ))

def display_regression_evaluation(evaluation):
    print('\tTraining evaluation results')

    headers = ['Model', 'R2 score', 'MSE', 'MAE']
    rows = []

    for key in evaluation:
        rows.append([key, evaluation[key]['r2_score'], evaluation[key]['mse'], evaluation[key]['mae']])

    print(tabulate(
        rows,
        headers = headers
    ))

def train_and_evaluate(models):
    evaluation = {}
    for key in models:
        evaluation[key] = models[key].train()
    
    return evaluation

def load_decoded_img(directory, name):
    img = image.load_img(directory + name)
    img = tf.image.encode_jpeg(image.img_to_array(img))
    return tf.io.encode_base64(img)