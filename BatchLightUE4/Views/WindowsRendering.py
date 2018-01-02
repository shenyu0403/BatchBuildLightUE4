# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsRendering.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Rendering(object):
    def setupUi(self, Rendering):
        Rendering.setObjectName("Rendering")
        Rendering.resize(400, 96)
        self.gridLayout = QtWidgets.QGridLayout(Rendering)
        self.gridLayout.setObjectName("gridLayout")
        self.label_level_name = QtWidgets.QLabel(Rendering)
        self.label_level_name.setObjectName("label_level_name")
        self.gridLayout.addWidget(self.label_level_name, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Rendering)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Rendering)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.label_level = QtWidgets.QLabel(Rendering)
        self.label_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_level.setObjectName("label_level")
        self.gridLayout.addWidget(self.label_level, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(Rendering)
        self.buttonBox.accepted.connect(Rendering.accept)
        self.buttonBox.rejected.connect(Rendering.reject)
        QtCore.QMetaObject.connectSlotsByName(Rendering)

    def retranslateUi(self, Rendering):
        _translate = QtCore.QCoreApplication.translate
        Rendering.setWindowTitle(_translate("Rendering", "Dialog"))
        self.label_level_name.setText(_translate("Rendering", "Level rendering name"))
        self.label_level.setText(_translate("Rendering", "Level Rendering :"))

