#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models

#Import Datasets
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Sequential API Model
model = keras.models.Sequential([
    layers.Flatten(input_shape = (28, 28)),
    layers.Dense(512, activation = "relu"),
    layers.Dense(256, activation = "relu"),
    layers.Dense(10),
])

#Compile process for the training of the Model
model.compile(
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    optimizer = keras.optimizers.Adam(learning_rate = 0.001),
    metrics = ["accuracy"]
)

#Fit datas to the Model
model.fit(x_train, y_train, batch_size = 64, epochs = 5, verbose = 1)

#Evaluate the Model with test datas
model.evaluate(x_test, y_test, batch_size = 32)

#Prediction of the test datas with np.argmax
prediction = model.predict(x_test, batch_size=32)
pred0 = prediction[1]
label0 = np.argmax(pred0)
print(label0)