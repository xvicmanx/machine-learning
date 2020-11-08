# Mall Customers Segmentation

## Description
This example solves an unsupervised problem of segmenting Mall customers based on their annual income and spending score.

## Dataset
The dataset is a csv file that contains 200 rows of customers information about their annual income and spending score.

```CustomerID,Gender,Age,Annual Income,Spending Score```

See `dataset.csv` for more details of the data.

## Solution
For this simple problem tested with the following models:
  1. K-Means clustering model.

## K-s clustering model selection

Different number of clusters were tried in from 1 to 10 clusters.
For each model the `Within cluster sum of squares (WCSS)` was computed.
Each of these results were plotted to create the `Elbow point graph`.
Then, the optimal number of clusters was selected from the graph.

<img src="persisted_models_data/k_means/elbow_point_graph_plot.png " width="350">

From the graph we can see that the optimal number is 5 clusters because it is where the WCSS stops decreasing significantly (an elbow is formed).

<img src="persisted_models_data/k_means/k_means_clustering_model_5_clusters_plot.png " width="350">

From the graph it can be noticed that the customers where divided in 5 groups:

1. Users with low income and low spending score (Cluster 4).

2. Users with low income and high spending score (Cluster 2).

3. Users with medium income and medium spending score (Cluster 1).

4. Users with high income and low spending score (Cluster 5)

5. Users with high income and high spending score (Cluster 3).

This information could be useful, for example campaigns to target users of high income but low spending score to see if they can increase their spending score.


## K-Means clusters assignments for each model variant (different number of clusters)

### 1 Cluster
<img src="persisted_models_data/k_means/k_means_clustering_model_1_clusters_plot.png " width="350">

### 2 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_2_clusters_plot.png " width="350">

### 3 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_3_clusters_plot.png " width="350">

### 4 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_4_clusters_plot.png " width="350">

### 5 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_5_clusters_plot.png " width="350">

### 6 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_6_clusters_plot.png " width="350">

### 7 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_7_clusters_plot.png " width="350">

### 8 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_8_clusters_plot.png " width="350">

### 9 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_9_clusters_plot.png " width="350">

### 10 Clusters
<img src="persisted_models_data/k_means/k_means_clustering_model_10_clusters_plot.png " width="350">

## Relevant files
- k_means_clustering_model.py: K-Means clustering model implementation for the problem.

- k_means_clustering_analysis.py: K-Means clustering analysis and model selection.

- dataset.csv: Dataset

- persisted_models_data: To store the trained models and graphs.