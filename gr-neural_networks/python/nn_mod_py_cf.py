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
import tensorflow as tf
import keras
from keras.models import model_from_json

class nn_mod_py_cf(gr.sync_block):
    """
    docstring for block nn_mod_py_cf
    """
    def __init__(self, model, weights):
        gr.sync_block.__init__(self,
            name="nn_mod_py_cf",
            # Take in IQ
            in_sig=[np.complex64],
            out_sig=[np.float32])

        self.set_model(model)
        self.set_weights(weights)

    def set_model(self, model):
        # Load in the Network Architecture
        json_file = open(model, 'r')
        model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(model_json)

        ws = 128
        self.window_size = ws
        self.window_i = np.zeros(self.window_size)
        self.window_q = np.zeros(self.window_size)

        # Set graph as global to be used across multiple threads
        global graph
        graph = tf.get_default_graph()

    def set_weights(self, weights):
        # Load in the Weights
        with graph.as_default():
            self.model.load_weights(weights)

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
                # We take in the Complex Number which is IQself.model.fit(np.reshape(self.window, self.i_rshape), np.reshape(np.array(x), (1, 1)), batch_size=1, epochs=1, verbose=0)
                i = x.real
                q = x.imag

                # Advance the Window I Window
                self.window_i[0:-1] = self.window_i[1:]
                self.window_i[-1] = i

                # Advance the Window Q Window
                self.window_q[0:-1] = self.window_q[1:]
                self.window_q[-1] = q

                # Now we need to construct the input window
                a = np.reshape(np.array(self.window_i), (1, self.window_size))
                b = np.reshape(np.array(self.window_q), (1, self.window_size))

                # Reshape the Input for the Model
                in_window = np.reshape(np.concatenate((a, b)), (1, 2, self.window_size))

                # Using the global graph do a prediction
                val = self.model.predict(in_window)

                # Append the results to the ouput
                out_vals.append(np.argmax(val, axis=1))

        # Reshape output into the correct size
        out[:] = np.reshape(np.array(out_vals), len(out))
        return len(output_items[0])

