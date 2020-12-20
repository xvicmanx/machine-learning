# Salary Prediction

## Description
This example solves the problem of predicting a person salary given the years of experience. 

## Dataset
The dataset is a csv file that contains 30 rows of years of experience - salary pair.

```YearsExperience,Salary```

See `salary.csv` for more details of the data.

## Solution
For this simple problem tested with the following models:
  1. Linear regression model.
  2. Polynomial regression model.
  3. Decision tree regression model.
  4. Random forest regression model.
  5. Support vector regression model.

## Results
Each model was evaluated with the R2 score.

| Model                                      | R2 score      |
| ------------------------------------------ | ------------- |
| Linear regression model                    | 0.9749        |
| Polynomial regression model (Degree 2)     | 0.9743        |
| Decision tree regression model             | 0.9100        |
| Random forest regression model             | 0.9438        |
| Support vector regression model (RBF)           | 0.9248        |


1. Linear regression model plot on test set

<img src="persisted_models_data/linear_regression_salary_prediction_model_plot.png " width="350">

2. Polynomial regression model plot on test set

<img src="persisted_models_data/polynomial_regression_salary_prediction_model_plot.png " width="350">

3. Decision tree regression model plot on test set

<img src="persisted_models_data/decision_tree_regression_salary_prediction_model_plot.png " width="350">

4. Random forest regression model plot on test set

<img src="persisted_models_data/random_forest_regression_salary_prediction_model_plot.png " width="350">

5. Support vector regression model plot on test set

<img src="persisted_models_data/support_vector_regression_salary_prediction_model_plot.png " width="350">


From the R2 score results and also from the plots we can see that the linear regressor is the one that best fits the problem data.

## Relevant files
- base_model.py: Regression model abstraction for the problem.

- linear_regression_model.py: Linear regression model implementation.

- polynomial_regression_model.py: Polynomial regression model implementation.

- decision_tree_regression_model.py: Decision tree regression model implementation.

- random_forest_regression_model.py: Random forest regression model implementation.

- support_vector_regression_model.py: Support vector regression model implementation.

- salary.csv: Dataset

- train.py: To train and persist the model.

- persisted_models_data: To store the trained models.