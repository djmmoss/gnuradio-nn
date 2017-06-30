#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Nn Online
# Generated: Fri Jun 30 19:46:50 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import neural_networks
import sip
import sys
from gnuradio import qtgui


class nn_online(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Nn Online")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Nn Online")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "nn_online")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.model_type = model_type = 'models/mlp.json'
        self.learn = learn = True

        ##################################################
        # Blocks
        ##################################################
        self._model_type_options = ('models/mlp.json', 'models/lstm.json', )
        self._model_type_labels = ('MLP', 'LSTM', )
        self._model_type_group_box = Qt.QGroupBox('Model')
        self._model_type_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._model_type_button_group = variable_chooser_button_group()
        self._model_type_group_box.setLayout(self._model_type_box)
        for i, label in enumerate(self._model_type_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._model_type_box.addWidget(radio_button)
        	self._model_type_button_group.addButton(radio_button, i)
        self._model_type_callback = lambda i: Qt.QMetaObject.invokeMethod(self._model_type_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._model_type_options.index(i)))
        self._model_type_callback(self.model_type)
        self._model_type_button_group.buttonClicked[int].connect(
        	lambda i: self.set_model_type(self._model_type_options[i]))
        self.top_layout.addWidget(self._model_type_group_box)
        _learn_check_box = Qt.QCheckBox('Learn')
        self._learn_choices = {True: True, False: False}
        self._learn_choices_inv = dict((v,k) for k,v in self._learn_choices.iteritems())
        self._learn_callback = lambda i: Qt.QMetaObject.invokeMethod(_learn_check_box, "setChecked", Qt.Q_ARG("bool", self._learn_choices_inv[i]))
        self._learn_callback(self.learn)
        _learn_check_box.stateChanged.connect(lambda i: self.set_learn(self._learn_choices[bool(i)]))
        self.top_layout.addWidget(_learn_check_box)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate/100, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.0)
        self.qtgui_time_sink_x_1.set_y_axis(0, 0.5)

        self.qtgui_time_sink_x_1.set_y_label('Error', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['Error', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	512, #size
        	samp_rate/100, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.0)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Prediction', 'Truth', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.neural_networks_nn_py_ff_0 = neural_networks.nn_py_ff(learn, model_type, 'modelu.h5')
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate/100,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 456, 2, -1)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 333, 0.5, -0.5)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 100, 2, 1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0, 2))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.neural_networks_nn_py_ff_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.neural_networks_nn_py_ff_0, 0), (self.blocks_delay_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "nn_online")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate/100)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/100)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/100)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_model_type(self):
        return self.model_type

    def set_model_type(self, model_type):
        self.model_type = model_type
        self._model_type_callback(self.model_type)
        self.neural_networks_nn_py_ff_0.set_model(self.model_type)

    def get_learn(self):
        return self.learn

    def set_learn(self, learn):
        self.learn = learn
        self._learn_callback(self.learn)
        self.neural_networks_nn_py_ff_0.set_learn(self.learn)


def main(top_block_cls=nn_online, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
