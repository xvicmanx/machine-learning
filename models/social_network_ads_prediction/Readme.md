# Purchase Prediction

## Description
This example solves the problem of predicting if a person is willing to purchase something based on his age and salary.

## Dataset
The dataset is a csv file that contains 400 rows containing information such as gender, age, estimated salary and a flag indicating if the user purchased a product or not.

```User ID,Gender,Age,EstimatedSalary,Purchased```

See `dataset.csv` for more details of the data.

## Solution
For this simple problem tested with the following models:
  1. Logistic Regression classification model.
  2. K Nearest Neighbor classification model.
  3. Decision Tree classification model.
  4. Random Forest classification model.
  5. Support Vector Machines classification model.
  6. Naive Bayes classification model.

## Results
Each model was evaluated based on the accuracy score, and confusion matrix.

| Model                                | Accuracy |
| -------------------------------------| ---------|
| Logistic Regression model            | 0.89     |
| K Nearest Neighbor                   | 0.93     |
| Decision tree classification model   | 0.91     |
| Random forest classification model   | 0.91     |
| Support vector machines model (RBF)  | 0.93     |
| Naive Bayes model                    | 0.90     |


1. Logistic Regression model plot on test set

<img src="persisted_models_data/logistic_regression_social_network_ads_prediction_model_plot.png " width="350">

2. K Nearest Neighbor model plot on test set

<img src="persisted_models_data/k_nearest_neighbor_social_network_ads_prediction_model_plot.png " width="350">

3. Decision tree classification model plot on test set

<img src="persisted_models_data/decision_tree_social_network_ads_prediction_model_plot.png " width="350">

4. Random forest classification model plot on test set

<img src="persisted_models_data/random_forest_social_network_ads_prediction_model_plot.png " width="350">

5. Support vector machines classification model plot on test set

<img src="persisted_models_data/support_vector_machines_social_network_ads_prediction_model_plot.png " width="350">

6. Support vector machines classification model plot on test set

<img src="persisted_models_data/naive_bayes_social_network_ads_prediction_model_plot.png " width="350">

### Confusion matrices


#### Logistic Regression model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 65        |   3     |
| [ 1 ]   | 8         | 24      |


#### Decision Tree model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 62        |   6     |
| [ 1 ]   | 3         | 29      |

#### Naive Bayes model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 65        |   3     |
| [ 1 ]   | 7         | 25      |


#### SVM model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 64        |   4     |
| [ 1 ]   | 3         | 29      |


#### Random Forest model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 62        |   6     |
| [ 1 ]   | 3         | 29      |


#### K Nearest Neighbor model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 64        |   4     |
| [ 1 ]   | 3         | 29      |


## Relevant files
- social_network_ads_base_model.py: Classification model abstraction for the problem.

- logistic_regression_classification_model.py: Logistic Regression classification model implementation for the problem.

- naive_bayes_classification_model.py: Naive bayes classification model implementation.

- decision_tree_classification_model.py: Decision tree classification model implementation.

- random_forest_classification_model.py: Random forest classification model implementation.

- svm_classification_model.py: Support vector machines classification model implementation.

- k_nearest_neighbor_classification_model.py: K nearest neighbor classification model implementation.

- dataset.csv: Dataset

- train.py: To train and persist the model the models

- persisted_models_data: To store the trained models and plot figures.