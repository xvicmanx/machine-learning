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
  3. Random forest regression model.

## Results
Each model was evaluated with the R2 score.

| Model                                      | R2 score      |
| ------------------------------------------ | ------------- |
| Linear regression model                    | 0.9749        |
| Polynomial regression model (Degree 2)     | 0.9743        |
| Decision tree regression model             | 0.9100        |
| Random forest regression model             | 0.9438        |

## Relevant files
- base_model.py: Regresion model abstraction for the problem.

- linear_regression_model.py: Linear regresion model implementation.

- polynomial_regression_model.py: Polynomial regresion model implementation.

- decision_tree_regression_model.py: Decision tree regresion model implementation.

- random_forest_regression_model.py: Random froest regresion model implementation.

- salary.csv: Dataset

- train.py: To train and persist the model.

- persisted_models_data: To store the trained models.