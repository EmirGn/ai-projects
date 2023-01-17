import tensorflow as tf
import pandas as pd
import numpy as np

from tensorflow import keras
from tensorflow.keras import datasets, models, layers

img_height = 28
img_weight = 28
batch_size = 2

model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, 3, padding = "same"),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding = "same"),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding = "same"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(6),
])

#                   METHOD - 1                  #
#-----------------------------------------------#
#           using dataset_from_directory        #
#-----------------------------------------------#

ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    "/Users/emirhangunyuzlu/Desktop/images",
    labels = "inferred",
    label_mode = "int",
    color_mode = "grayscale",
    batch_size = batch_size,
    image_size = (img_height, img_weight),
    shuffle = True,
    seed = 200,
    validation_split = 0.1,
    subset = "training",

)

ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
    "/Users/emirhangunyuzlu/Desktop/images",
    labels="inferred",
    label_mode="int",
    color_mode="grayscale",
    batch_size=batch_size,
    image_size=(img_height, img_weight),
    shuffle=True,
    seed=200,
    validation_split=0.1,
    subset="validation",

)

def augment(x, y):
    image = tf.image.random_brightness(x, max_delta=0.05)
    return image, y

ds_train = ds_train.map(augment)

for epochs in range (10):
    for x, y in ds_train:
        pass


model.compile(
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    optimizer = keras.optimizers.Adam(learning_rate = 0.001),
    metrics = ["accuracy"],
)

model.fit(ds_train, epochs = 5, verbose = 1)