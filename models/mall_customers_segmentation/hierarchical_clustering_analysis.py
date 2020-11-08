import os, sys
import matplotlib.pyplot as plt

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from hierarchical_clustering_model import HierarchichalClusteringModel


title = 'Hierarchical clustering model'

print(title + ': Start')



model = HierarchichalClusteringModel()

model.plot_dendogram()

print('\nSaving model')

model.train()
model.save()

print(title + ': End')