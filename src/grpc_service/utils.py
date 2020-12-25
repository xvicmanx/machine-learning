import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

def preprocess_and_decode(img_str):
  img = tf.io.decode_base64(img_str)
  img = tf.image.decode_jpeg(img, channels = 3)
  img = tf.image.resize(img, (64, 64))

  generator = image.ImageDataGenerator(rescale = 1. / 255)

  return generator.flow(np.array([image.img_to_array(img)]))

