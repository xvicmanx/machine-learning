import os, sys
import matplotlib.pyplot as plt

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from k_means_clustering_model import KMeansClusteringModel


def train_and_evaluate_clustering_models(max_number_of_clusters = 10):
    models = []
    n = max_number_of_clusters + 1

    for number_of_clusters in range(1, n):
        model = KMeansClusteringModel(number_of_clusters = number_of_clusters)
        models.append(model)  

    wcss = []
    for i in range(0, len(models)):
        evaluation = models[i].train()
        wcss.append(evaluation['wcss'])  

    plt.plot(range(1, n), wcss)
    plt.title('Elbow point graph')
    plt.xlabel('Number of clusters')
    plt.ylabel('Within cluster sum of squares (WCSS)')
    plt.savefig(currentdir + '/persisted_models_data/k_means/elbow_point_graph_plot.png')
    plt.clf()

    return models

title = 'K-Means clustering models'

print(title + ': Start')

models = train_and_evaluate_clustering_models()

print('\nSaving models')

for i in range(0, len(models)):
   models[i].save()

print(title + ': End')