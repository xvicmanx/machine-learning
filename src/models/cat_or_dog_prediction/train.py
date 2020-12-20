import os, sys
import numpy as np
from tensorflow.keras.preprocessing import image

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
sys.path.append(os.path.dirname(parent_dir))

from helpers import train_and_evaluate, display_predictions, display_classification_evaluation

from neural_network_classification_model import NeuralNetworkCatOrDogPredictionModel

title = 'Training cat or dog pred models'

print(title + ': Start')

models = {
    'Neural Network Model': NeuralNetworkCatOrDogPredictionModel()
}

evaluation = train_and_evaluate(models)

print(title + ': End')

display_classification_evaluation(evaluation)

cat_image = image.load_img(current_dir + '/datasets/cat.jpg', target_size = (64, 64))
dog_image = image.load_img(current_dir + '/datasets/puppy.jpg', target_size = (64, 64))

gen = image.ImageDataGenerator(rescale = 1. / 255)

iterator = gen.flow(np.array([
    image.img_to_array(cat_image),
    image.img_to_array(dog_image),
]))

display_predictions(
    models,
    iterator,
    False,
)

print('\nSaving models')


for key in models:
   models[key].save()
