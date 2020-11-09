# Optimal Campaign Ad search

## Description
This example solves the problem of finding the optimal ad for a campaign that contains 10 ads to choose from.

## Dataset
The dataset is a csv file that contains 10,000 rows of simulation of the likelihood of a customer to click a given Ad. Each row correspond to a given user.

```Ad 1,Ad 2,Ad 3,Ad 4,Ad 5,Ad 6,Ad 7,Ad 8,Ad 9,Ad 10```

See `dataset.csv` for more details of the data.

## Solution
For this problem it was tested with the following models:
  1. Upper Confidence Bound model.

## Results

### Upper Confidence Bound model
For Upper Confidence Bound model after finishing the training, it has converged to an optimal option that is the fifth one.

<img src="persisted_models_data/upper_confidence_bound_opt_ad_search_model_plot.png " width="350">

## Results

## Relevant files

- upper_confidence_bound_model.py: Upper Confidence Bound model implementation.

- dataset.csv: Dataset

- train.py: To train and persist the model.

- persisted_models_data: To store the trained models.