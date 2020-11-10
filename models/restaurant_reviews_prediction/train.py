import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from helpers import  train_and_evaluate, display_predictions, display_classification_evaluation

from naive_bayes_classification_model import NaiveBayesRestaurantReviewsPredictionModel


title = 'Training Restaurant reviews prediction models'

print(title + ': Start')

models = {
    'Naive Bayes Model': NaiveBayesRestaurantReviewsPredictionModel(),
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_classification_evaluation(evaluation)
display_predictions(
    models,
    [
        ['Very good my friend'],
        ['The food was tasty'],
        ['The food was bad'],
    ],
)

print('\nSaving models')


for key in models:
   models[key].save()
