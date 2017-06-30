#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from tqdm import *


import keras
from keras import backend as K
from keras.layers import Dense, LSTM, Embedding
from keras.objectives import categorical_crossentropy
import keras.models as models
from keras.layers.core import Reshape, Activation
from keras.regularizers import *
from keras.optimizers import adam
from keras.utils import np_utils

def make_data(data, window_size):
	X = []

	win_size = window_size + 1
	for i in range(len(data)-win_size):
		X.append(data[i:i+win_size])

	return np.array(X)

def train_test_split(data, window_size, perc=0.6):

	window_data = make_data(data, window_size)

	itrn = int(len(data)*0.6)
	train = window_data[:itrn, :]
	np.random.shuffle(train)
	X_train = train[:, :-1]
	Y_train = train[:, -1]
	X_test = window_data[itrn:, :-1]
	Y_test = window_data[itrn:, -1]

	return X_train, Y_train, X_test, Y_test


def predict_sequence(model, start, length):
	window = start
	res = np.zeros(length)
	for i in tqdm(range(length)):
		# Predict the next time step
		res[i] = model.predict(np.reshape(window, (1, window.shape[0])))

		# Shift the Window with the predictions
		window[0:-1] = window[1:]
		window[-1] = res[i]
	return res

window_size = 50
in_shp = list([window_size])

model = models.Sequential()
model.add(Dense(16, input_shape=in_shp))
model.add(Dense(units=1, activation="linear"))
model.summary()

model.compile(loss='mean_squared_error',
	      optimizer='rmsprop')


t = np.arange(0, 10000.0, 0.1)
x1 = np.sin(2*t + 4)
x2 = np.sin(t*0.3)

x = x1 + x2

X_train, Y_train, X_test, Y_test = train_test_split(x, window_size)

model.fit(X_train, Y_train, batch_size=50, epochs=10, validation_split=0.05)
score = model.evaluate(X_test, Y_test)
print("Test Score:", score)

test_prediction = model.predict(X_test)

p_sequence = predict_sequence(model, X_test[0], X_test.shape[0])

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# serialize model weights
model.save_weights('model.h5')
