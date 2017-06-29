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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from nn_py_ff import nn_py_ff

import numpy as np
import keras
from pylab import *

class qa_nn_py_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
    	# set up fg
        t = np.arange(0, 200.0, 0.1)
        x = np.sin(t)
        src_data = x[:-1]
        expected_result = x[1:]
        src = blocks.vector_source_f(src_data)
        mlp = nn_py_ff(True, 'model.json', 'modelo.h5')
        snk = blocks.vector_sink_f()
        self.tb.connect(src, mlp)
        self.tb.connect(mlp, snk)
        self.tb.run()
        next_data = snk.data()

        # Only check the last 100 results
        n_plot = 100
        _, axarr = plt.subplots(3, sharex=True, sharey=True)
        axarr[0].plot(expected_result[-n_plot:])
        axarr[0].set_title('Test Observation')
        axarr[1].plot(next_data[-n_plot:])
        axarr[1].set_title('Prediction')
        axarr[2].plot(expected_result[-n_plot:])
        axarr[2].plot(next_data[-n_plot:])
        axarr[2].set_title('Test Observation and Prediction')
        plt.show()

        # check data
        self.assertFloatTuplesAlmostEqual(expected_result[-n_plot:], next_data[-n_plot:], 1)


if __name__ == '__main__':
    gr_unittest.run(qa_nn_py_ff, "qa_nn_py_ff.xml")
