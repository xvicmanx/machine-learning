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

| Model                                | Accuracy | F0.5 Score | F1 Score | F2 Score |
| -------------------------------------| ---------|------------|----------|----------|
| Logistic Regression model            | 0.89     | 0.86       | 0.81     | 0.77     |
| K Nearest Neighbor                   | 0.93     | 0.88       | 0.89     | 0.90     |
| Decision tree classification model   | 0.91     | 0.84       | 0.87     | 0.89     |
| Random forest classification model   | 0.91     | 0.84       | 0.86     | 0.89     |
| Support vector machines model (RBF)  | 0.93     | 0.88       | 0.89     | 0.90     |
| Naive Bayes model                    | 0.90     | 0.84       | 0.87     | 0.89     |



### Confusion matrices and plots


#### Logistic Regression model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 65        |   3     |
| [ 1 ]   | 8         | 24      |

<img src="persisted_models_data/logistic_regression_social_network_ads_prediction_model_plot.png " width="350">

#### Decision Tree model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 62        |   6     |
| [ 1 ]   | 3         | 29      |

<img src="persisted_models_data/decision_tree_social_network_ads_prediction_model_plot.png " width="350">

#### Naive Bayes model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 65        |   3     |
| [ 1 ]   | 7         | 25      |
<img src="persisted_models_data/naive_bayes_social_network_ads_prediction_model_plot.png " width="350">

#### SVM model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 64        |   4     |
| [ 1 ]   | 3         | 29      |


<img src="persisted_models_data/support_vector_machines_social_network_ads_prediction_model_plot.png " width="350">

#### Random Forest model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 62        |   6     |
| [ 1 ]   | 3         | 29      |

<img src="persisted_models_data/random_forest_social_network_ads_prediction_model_plot.png " width="350">

#### K Nearest Neighbor model

|         | Predicted |    |
| --------| ----------|----|
| Actual  | [ 0 ]     | [ 1  ]  |
| [ 0 ]   | 64        |   4     |
| [ 1 ]   | 3         | 29      |

<img src="persisted_models_data/k_nearest_neighbor_social_network_ads_prediction_model_plot.png " width="350">

Based on the metrics of accuracy, f0.5, f1, and f2 scores, the winning models are SVM and K Nearest Neighbors with a tie: 0.93, 0,88, 0.89, 0.90.

These models beat the others.


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