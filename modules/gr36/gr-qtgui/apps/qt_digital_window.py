# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_digital_window.ui'
#
# Created: Sat May  1 20:14:02 2010
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_DigitalWindow(object):

    def setupUi(self, DigitalWindow):
        DigitalWindow.setObjectName("DigitalWindow")
        DigitalWindow.resize(1236, 741)
        self.centralwidget = QtGui.QWidget(DigitalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sinkFrame = QtGui.QFrame(self.centralwidget)
        self.sinkFrame.setMinimumSize(QtCore.QSize(0, 550))
        self.sinkFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sinkFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sinkFrame.setObjectName("sinkFrame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.sinkFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sinkLayout = QtGui.QHBoxLayout()
        self.sinkLayout.setObjectName("sinkLayout")
        self.horizontalLayout_2.addLayout(self.sinkLayout)
        self.verticalLayout.addWidget(self.sinkFrame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sysBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sysBox.sizePolicy().hasHeightForWidth())
        self.sysBox.setSizePolicy(sizePolicy)
        self.sysBox.setMinimumSize(QtCore.QSize(0, 0))
        self.sysBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.sysBox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.sysBox.setObjectName("sysBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.sysBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sampleRateEdit = QtGui.QLineEdit(self.sysBox)
        self.sampleRateEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sampleRateEdit.setObjectName("sampleRateEdit")
        self.gridLayout_2.addWidget(self.sampleRateEdit, 0, 3, 1, 1)
        self.sampleRateLabel = QtGui.QLabel(self.sysBox)
        self.sampleRateLabel.setObjectName("sampleRateLabel")
        self.gridLayout_2.addWidget(self.sampleRateLabel, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.sysBox)
        self.rxBox = QtGui.QGroupBox(self.centralwidget)
        self.rxBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.rxBox.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.rxBox.setObjectName("rxBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.rxBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.alphaLabel = QtGui.QLabel(self.rxBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.gridLayout_3.addWidget(self.alphaLabel, 1, 0, 1, 1)
        self.alphaEdit = QtGui.QLineEdit(self.rxBox)
        self.alphaEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.alphaEdit.setObjectName("alphaEdit")
        self.gridLayout_3.addWidget(self.alphaEdit, 1, 1, 1, 1)
        self.gainMuLabel = QtGui.QLabel(self.rxBox)
        self.gainMuLabel.setObjectName("gainMuLabel")
        self.gridLayout_3.addWidget(self.gainMuLabel, 0, 0, 1, 1)
        self.gainMuEdit = QtGui.QLineEdit(self.rxBox)
        self.gainMuEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.gainMuEdit.setObjectName("gainMuEdit")
        self.gridLayout_3.addWidget(self.gainMuEdit, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.rxBox)
        self.channelModeBox = QtGui.QGroupBox(self.centralwidget)
        self.channelModeBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.channelModeBox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.channelModeBox.setObjectName("channelModeBox")
        self.gridLayout = QtGui.QGridLayout(self.channelModeBox)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.snrLabel = QtGui.QLabel(self.channelModeBox)
        self.snrLabel.setObjectName("snrLabel")
        self.gridLayout.addWidget(self.snrLabel, 0, 1, 1, 1)
        self.snrEdit = QtGui.QLineEdit(self.channelModeBox)
        self.snrEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.snrEdit.setObjectName("snrEdit")
        self.gridLayout.addWidget(self.snrEdit, 0, 2, 1, 1)
        self.freqLabel = QtGui.QLabel(self.channelModeBox)
        self.freqLabel.setObjectName("freqLabel")
        self.gridLayout.addWidget(self.freqLabel, 1, 1, 1, 1)
        self.freqEdit = QtGui.QLineEdit(self.channelModeBox)
        self.freqEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.freqEdit.setObjectName("freqEdit")
        self.gridLayout.addWidget(self.freqEdit, 1, 2, 1, 1)
        self.timeLabel = QtGui.QLabel(self.channelModeBox)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 2, 1, 1, 1)
        self.timeEdit = QtGui.QLineEdit(self.channelModeBox)
        self.timeEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 2, 2, 1, 1)
        self.horizontalLayout.addWidget(self.channelModeBox)
        spacerItem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pauseButton.setObjectName("pauseButton")
        self.verticalLayout_2.addWidget(self.pauseButton)
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_2.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DigitalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DigitalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        DigitalWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DigitalWindow)
        self.statusbar.setObjectName("statusbar")
        DigitalWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(DigitalWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(DigitalWindow)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(
            "clicked()"), DigitalWindow.close)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(
            "triggered()"), DigitalWindow.close)
        QtCore.QMetaObject.connectSlotsByName(DigitalWindow)
        DigitalWindow.setTabOrder(self.snrEdit, self.freqEdit)
        DigitalWindow.setTabOrder(self.freqEdit, self.timeEdit)

    def retranslateUi(self, DigitalWindow):
        DigitalWindow.setWindowTitle(QtGui.QApplication.translate(
            "DigitalWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.sysBox.setTitle(QtGui.QApplication.translate(
            "DigitalWindow", "System Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.sampleRateLabel.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Sample Rate (sps)", None, QtGui.QApplication.UnicodeUTF8))
        self.rxBox.setTitle(QtGui.QApplication.translate(
            "DigitalWindow", "Receiver Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.alphaLabel.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.gainMuLabel.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Gain mu", None, QtGui.QApplication.UnicodeUTF8))
        self.channelModeBox.setTitle(QtGui.QApplication.translate(
            "DigitalWindow", "Channel Model Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.snrLabel.setText(QtGui.QApplication.translate(
            "DigitalWindow", "SNR (dB)", None, QtGui.QApplication.UnicodeUTF8))
        self.freqLabel.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Frequency Offset (Hz)", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Timing Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseButton.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate(
            "DigitalWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate(
            "DigitalWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate(
            "DigitalWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
