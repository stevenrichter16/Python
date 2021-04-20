# -*- coding: utf-8 -*-
"""a5.ipynb

# Training a Multilayer Neural Network for Image Classification

# Accuracy = .985

## First, let's import the necessary packages
"""

import sys, os
import sklearn
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# Ignore useless warnings 
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")

"""Fashion MNIST is a collection of 70,000 grayscale images of 28x28 pixels (each with intensity in the range 0-255), each with 10 classes. The images represent fashion items. Keras provides a utility function to preload this data set directly, with the data set already broken into train and test sets"""

fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.mnist.load_data()

"""Let's look at the shape and data of the training set"""

X_train_full.shape

X_train_full.dtype

"""Instead of eventually doing cross validation on the training set, let's further break the training set into a training set and a validation set, as this is more reliable, if we have the data to do it. Let's also scale the intensities of each pixel to be in the range 0-1.

"""

X_valid, X_train = X_train_full[:5000] / 255., X_train_full[5000:] / 255.
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.

"""Let's look at the first image in the training set:"""

plt.imshow(X_train[0], cmap="binary")
plt.axis('off')
plt.show()

"""The labels are numbers that correspond to the class names"""

y_train

"""Here are the corresponding class names:"""

class_names = [0, 1, 2, 3, 4,
               5, 6, 7, 8, 9]
class_names[y_train[0]]

"""Let's look at the sizes for our train, validation and test sets:"""

X_train.shape

X_valid.shape

X_test.shape

"""Let's take a look at a sample of the images in the dataset:"""

n_rows = 4
n_cols = 10
plt.figure(figsize=(n_cols * 1.2, n_rows * 1.2))
for row in range(n_rows):
    for col in range(n_cols):
        index = n_cols * row + col
        plt.subplot(n_rows, n_cols, index + 1)
        plt.imshow(X_train[index], cmap="binary", interpolation="nearest")
        plt.axis('off')
        plt.title(class_names[y_train[index]], fontsize=12)
plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()

"""Let's build a neural network with two hidden layers. Let's setup our random seeds for reproducibility"""

keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

"""Let's use the simplest sequential model. 
* We build our input layer that flattens the images into a 1D array.
* Next we add a dense hidden layer with 300 neurons; it manages its own weight matrix and bias terms, and uses the ReLU activation function.
* Then we add a second hidden layer with 100 neurons and the ReLU activation function.
* Finally, we add the output layer with 10 neurons (for the 10 output classes). Since we must choose one of those 10 classes, we use the softmax activation function, rather than the sigmoid activation function. Softmax can handle the multinomial classification problem. 



"""

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(512, activation="relu"))
model.add(keras.layers.Dense(256, activation="relu"))
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))

"""You can look at textual and visual summaries of the model"""

model.summary()

"""You can access the model's layers and individual layers as below. """

model.layers

"""After a model is created, you must call its compile() method to specify the loss function and optimizer to use. You can also optionally specify extra metrics to compute during training and evaluation.
*  We use "sparse_categorical_crossentropy" because we have sparse labels (for each instance, there is just a target class index from 0-9). If we were doing binary classification, then we would use the sigmoid activation function (instead of softmax), and we would use "binary_crossentropy"
* We will train the model using simple stochastic gradient descent  with a learning rate of 0.01 and momentum of 0. There are multiple parameters you can specify here.
* Since this is a classifier, it's useful to measure the accuracy during training and evaluation
"""

model.compile(loss="sparse_categorical_crossentropy",
              optimizer=keras.optimizers.SGD(lr=0.01,momentum=0.9),
              metrics=["accuracy"])

"""To train the model, we simply call the fit function. 
* We specify the epochs, and we provide our validation set. Since we have this validation set, we will not use cross validation. The training reports a training and validation loss and accuracy.
* Note that the fit() method uses a batch size of 32 as default if you do not explicitly specify that. This means that 32 sampled instances are used per epoch, and not the full training set. It has been shown that using the full training set can lead to models that generalize poorly. But you can certainly try batch sizes greater than 32, ideally in powers of 2.
"""

history = model.fit(X_train, y_train, epochs=45,batch_size=32, 
                    validation_data=(X_valid, y_valid))

"""The fit() method returns a history object that contains the training parameters, list of epochs, it went rhough, and a dictionary containing the loss and extra metrics measured at the end of each epoch. """

history.params

print(history.epoch)

history.history.keys()

"""You can use this data to plot the bias-variance curve. You can see that we have still not overfit the model, so we could probably keep training for more epochs.
The validation set loss plot serves as our Test data line in the graph in the Performance Evaluation lecture, while the training set loss plot serves as the CV line in our graph in lecture
"""

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.show()

"""If you are not satisfied with your model perfomance,
* first tune the hyperparameters, starting with the learning rate, and then other hyper parameters
* if that does not help, then tune the model parameters such as the number of layers, number of neurons per layer, and the types of activation functions for each hidden layer
* You can also try tuning the batch size hyperparameter

Once you are satisfied with the model's performance, evaluate it on the test set to estimate the generalization error using the evaluate() method
"""

model.evaluate(X_test, y_test)

"""Next, use the predict() method to make predictions. Since we don't have new instances, let's just use the first 3 instances of the test set."""

X_new = X_test[:3]
y_proba = model.predict(X_new)
y_proba.round(2)

"""As you can see above, for each instance the model estimates one probability per class from class 0 to class 9. 

So the first image is class 9 (ankle boot) with 96% probability and class 7 (sneaker) with 3% probability. 

If you only care about the class with the highest estimated probability (even if that probability is quite low), then you can use the predict_classes() method instead
"""

y_pred = model.predict_classes(X_new)
y_pred

np.array(class_names)[y_pred]

"""Here the classifier classified all three images correctly."""

y_new = y_test[:3]
y_new

"""And we can see the actual images too"""

plt.figure(figsize=(7.2, 2.4))
for index, image in enumerate(X_new):
    plt.subplot(1, 3, index + 1)
    plt.imshow(image, cmap="binary", interpolation="nearest")
    plt.axis('off')
    plt.title(class_names[y_test[index]], fontsize=12)
plt.subplots_adjust(wspace=0.2, hspace=0.5)
plt.show()

"""So hopefully this gives you an idea of how to set up a multilayer neural network using tensor flow and keras"""