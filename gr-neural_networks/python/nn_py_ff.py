#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr

import os.path

import tensorflow as tf
import keras
from keras.models import model_from_json

class nn_py_ff(gr.sync_block):
    """
    docstring for block nn_py_ff
    """
    def __init__(self, learn=False, model="model.json", weights="model.h5"):
        gr.sync_block.__init__(self,
            name="nn_py_ff",
            in_sig=[np.float32],
            out_sig=[np.float32])

        # Flag if we are going to do Online Learning
        self.set_learn(learn)
        self.set_model(model)
        self.set_weights(weights)

    def set_learn(self, learn):
        self.learn = learn

    def set_model(self, model):
        # Load in the Network Architecture
        json_file = open(model, 'r')
        model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(model_json)

        self.model.compile(loss='mean_squared_error', optimizer='rmsprop')
        input_shape = self.model.layers[0].input_shape
        output_shape = self.model.layers[0].output_shape
        input_dim = len(self.model.layers[0].input_shape)

        if input_dim == 2:
            # MLP
            ws = input_shape[-1]
            rshape = (1, ws)
        elif input_dim == 3:
            ws = output_shape[-1]
            rshape = (1, ws, 1)

        self.window_size = ws
        self.window = np.zeros(self.window_size)

        self.i_rshape = rshape

        # Set graph as global to be used across multiple threads
        global graph
        graph = tf.get_default_graph()

    def set_weights(self, weights):
        # Load in the Weights
        with graph.as_default():
            if os.path.isfile(weights):
                self.model.load_weights(weights)

    def make_data(self, data, window_size):
        X = []

        win_size = window_size + 1
        for i in range(len(data)-win_size):
            X.append(data[i:i+win_size])

        return np.array(X)

    def data_split(self, data, window_size):

        window_data = self.make_data(data, window_size)

        X = window_data[:, :-1]
        Y = window_data[:, -1]
        final_window = np.concatenate((X[-1,1:], np.array([Y[-1]])))
        X = np.concatenate((X, np.array([final_window])))

        return X, Y

        
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # Bring in the global graph
        global graph

        # Create a clear output values list
        out_vals = []

       # For each input element - Do a prediction 
        for x in in0:
            with graph.as_default():
                # Online Learning Step
                if self.learn:
                    self.model.fit(np.reshape(self.window, self.i_rshape), np.reshape(np.array(x), (1, 1)), batch_size=1, epochs=1, verbose=0)

                # Advance the Window
                self.window[0:-1] = self.window[1:]
                self.window[-1] = x

                #print(i)

                # Reshape the Input for the Model
                in_window = np.reshape(self.window, self.i_rshape)

                # Using the global graph do a prediction
                val = self.model.predict(in_window)

                # Append the results to the ouput
                out_vals.append(val)

        # Reshape output into the correct size
        out[:] = np.reshape(np.array(out_vals), len(out))
        return len(output_items[0])
