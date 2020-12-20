# Restaurant Reviews Prediction

## Description
This example solves the problem of predicting whether a review was positive or negative based on the review comments.

## Dataset
The dataset is a tsv file that contains 1000 rows reviews that contain an output column (`Liked`) indicating if the review was positive or not (1 or 0).

```Review Liked```

See `dataset.tsv` for more details of the data.

## Solution
For this problem it was tested with the following models:
  1. Naive Bayes classification model.
  2. Decision Tree classification model.
  3. Support Vector Machine classification model.

## Results
Each model was evaluated based on the accuracy score, and confusion matrix.

| Model                                | Accuracy | F0.5 Score | F1 Score | F2 Score |
| -------------------------------------| ---------|------------|----------|----------|
| Decision tree classification model   | 0.78     | 0.79       | 0.78     | 0.77     |
| Support vector machines model (RBF)  | 0.86     | 0.88       | 0.86     | 0.84     |
| Naive Bayes model                    | 0.73     | 0.72       | 0.77     | 0.83     |



### Confusion matrices


#### Decision Tree model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 78        |  19     |
| [ 1 ]   | 25        |  78     |

#### Naive Bayes model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 55        |  42     |
| [ 1 ]   | 12        |  91     |

#### SVM model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 86        |   11    |
| [ 1 ]   | 17        |   86    |


Based on the metrics of accuracy, f0.5, f1, and f2 scores, the winning model is SVM with the values: 0.96, 0,88, 0.86, 0.84.


## Relevant files
- restaurant_reviews_prediction_base_model.py: Classification model abstraction for the problem.

- naive_bayes_classification_model.py: Naive bayes classification model implementation.

- decision_tree_classification_model.py: Decision tree classification model implementation.

- svm_classification_model.py: Support vector machines classification model implementation.

- dataset.tsv: Dataset

- train.py: To train and persist the model the models

- persisted_models_data: To store the trained models.