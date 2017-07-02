#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Nn Mod
# Generated: Sun Jul  2 12:24:23 2017
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


class NN_MOD(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Nn Mod")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Nn Mod")
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

        self.settings = Qt.QSettings("GNU Radio", "NN_MOD")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e3
        self.data_file = data_file = 'data/bpsk.bin'

        ##################################################
        # Blocks
        ##################################################
        self._data_file_options = ('data/pam4.bin', 'data/bpsk.bin', 'data/am-dsb.bin', 'data/cpfsk.bin', )
        self._data_file_labels = ('PAM4', 'BPSK', 'AM-DSB', 'CPFSK', )
        self._data_file_group_box = Qt.QGroupBox('Modulation Type')
        self._data_file_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._data_file_button_group = variable_chooser_button_group()
        self._data_file_group_box.setLayout(self._data_file_box)
        for i, label in enumerate(self._data_file_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._data_file_box.addWidget(radio_button)
        	self._data_file_button_group.addButton(radio_button, i)
        self._data_file_callback = lambda i: Qt.QMetaObject.invokeMethod(self._data_file_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._data_file_options.index(i)))
        self._data_file_callback(self.data_file)
        self._data_file_button_group.buttonClicked[int].connect(
        	lambda i: self.set_data_file(self._data_file_options[i]))
        self.top_layout.addWidget(self._data_file_group_box)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	12 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.0)
        self.qtgui_time_sink_x_0.set_y_axis(0, 10)

        self.qtgui_time_sink_x_0.set_y_label('Modulation Type', '')

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Input', 'WBFM', 'QPSK', 'QAM64', 'QAM16',
                  'PAM4', 'GFSK', 'CPFSK', 'BPSK', 'AM-SBB', 'AM-DSB', '8PSK']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "cyan", "black",
                  "magenta", "yellow", "dark red", "dark green", "cyan", "black", "green"]
        styles = [1, 3, 2, 2, 2,
                  2, 2, 2, 2, 3, 3, 2]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1, -1, -1]
        alphas = [1.0, 0.7, 0.7, 0.7, 0.7,
                  0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]

        for i in xrange(12):
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
        self.neural_networks_nn_mod_py_cf_0 = neural_networks.nn_mod_py_cf('models/conv.json', 'weights/convmodrecnets_CNN2_0.5.wts.h5')
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, data_file, True)
        self.analog_const_source_x_0_1_7 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0_1_6 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0_1_5 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 2)
        self.analog_const_source_x_0_1_4 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 3)
        self.analog_const_source_x_0_1_3 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 4)
        self.analog_const_source_x_0_1_2 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 5)
        self.analog_const_source_x_0_1_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 6)
        self.analog_const_source_x_0_1_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 7)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 8)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 9)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 10)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.analog_const_source_x_0_1, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.analog_const_source_x_0_1_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.analog_const_source_x_0_1_1, 0), (self.qtgui_time_sink_x_0, 5))
        self.connect((self.analog_const_source_x_0_1_2, 0), (self.qtgui_time_sink_x_0, 6))
        self.connect((self.analog_const_source_x_0_1_3, 0), (self.qtgui_time_sink_x_0, 7))
        self.connect((self.analog_const_source_x_0_1_4, 0), (self.qtgui_time_sink_x_0, 8))
        self.connect((self.analog_const_source_x_0_1_5, 0), (self.qtgui_time_sink_x_0, 9))
        self.connect((self.analog_const_source_x_0_1_6, 0), (self.qtgui_time_sink_x_0, 10))
        self.connect((self.analog_const_source_x_0_1_7, 0), (self.qtgui_time_sink_x_0, 11))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.neural_networks_nn_mod_py_cf_0, 0))
        self.connect((self.neural_networks_nn_mod_py_cf_0, 0), (self.qtgui_time_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "NN_MOD")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_data_file(self):
        return self.data_file

    def set_data_file(self, data_file):
        self.data_file = data_file
        self._data_file_callback(self.data_file)
        self.blocks_file_source_0.open(self.data_file, True)


def main(top_block_cls=NN_MOD, options=None):

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
