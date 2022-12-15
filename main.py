import keras.models
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images, test_images = train_images / 255, test_images / 255

model1 = keras.models.load_model("nn.h5")

test_loss, test_acc = model1.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model1,
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

predictions[0]

img = cv.imread("canta.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img, cmap = plt.cm.binary)

img = np.array(img)/255
img = np.mean(img, axis=-1)

img = img[np.newaxis, ...]
prediction = model1.predict(img)
index = np.argmax(prediction)
print(f"Prediction is {class_names[index]}")