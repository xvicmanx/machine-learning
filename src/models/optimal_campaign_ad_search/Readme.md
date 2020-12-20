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
  2. Thompson Sampling model

## Results

### Upper Confidence Bound model
For Upper Confidence Bound model after finishing the training, it has converged to an optimal option that is the fifth one.

<img src="persisted_models_data/upper_confidence_bound_opt_ad_search_model_plot.png " width="350">

The UCB for 500 hundred rounds could not converge to the optimal value.
<img src="persisted_models_data/upper_confidence_bound_opt_ad_search_500_rounds_model_plot.png " width="350">

### Thompson Sampling model
For Thompson Sampling model after finishing the training, it has also converged to an optimal option that is the fifth one.

<img src="persisted_models_data/thompson_sampling_opt_ad_search_model_plot.png " width="350">

The Thompson sampling model has converged faster than the UCB as it is shown in the following graph that correspond to 500 rounds.
<img src="persisted_models_data/thompson_sampling_opt_ad_search_500_rounds_model_plot.png " width="350">

## Relevant files

- optimal_campaign_ad_search_base_model.py: Optimal Campaign Ad search base model.

- upper_confidence_bound_model.py: Upper Confidence Bound model implementation.

- thompson_sampling_model.py: Thompson Samplin model implementation.

- dataset.csv: Dataset

- train.py: To train and persist the model.

- persisted_models_data: To store the trained models.