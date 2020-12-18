import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from helpers import  train_and_evaluate, display_predictions, display_classification_evaluation

from naive_bayes_classification_model import NaiveBayesRestaurantReviewsPredictionModel
from decision_tree_classification_model import DecisionTreeRestaurantReviewsPredictionModel
from svm_classification_model import SupportVectorMachinesRestaurantReviewsPredictionModel


title = 'Training Restaurant reviews prediction models'

print(title + ': Start')

models = {
    'Naive Bayes Model': NaiveBayesRestaurantReviewsPredictionModel(),
    'Decision Tree Model': DecisionTreeRestaurantReviewsPredictionModel(),
    'SVM Model': SupportVectorMachinesRestaurantReviewsPredictionModel(),
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_classification_evaluation(evaluation)
display_predictions(
    models,
    [
        ['Very good my friend'],
        ['The food was very tasty'],
        ['The food was bad'],
    ],
)

print('\nSaving models')


for key in models:
   models[key].save()
