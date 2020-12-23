import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
# Appending parent dir
sys.path.append(os.path.dirname(currentdir))

from som_model import SOMModel

title = 'Animals SOM'

print(title + ': Start')

size = 3
model = SOMModel(size)

model.train()

results = {}

for i in range(size):
  for j in range(size):
    key = str((i, j))
    if results.get(key) is None:
      results[key] = []

for item in model.dataset().iloc[:, :].values:
  position = model.predict(list(item[1:]))
  key = str(position)
  results[key].append(item[0])


for i in range(size):
  for j in range(size):
    key = str((i, j))
    print(key, results[key])

print('\nSaving model')

print(title + ': End')