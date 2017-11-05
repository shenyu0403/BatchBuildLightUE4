# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsLogView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogLog(object):
    def setupUi(self, DialogLog):
        DialogLog.setObjectName("DialogLog")
        DialogLog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogLog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DialogLog)
        self.label.setGeometry(QtCore.QRect(110, 90, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(DialogLog)
        self.buttonBox.accepted.connect(DialogLog.accept)
        self.buttonBox.rejected.connect(DialogLog.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogLog)

    def retranslateUi(self, DialogLog):
        _translate = QtCore.QCoreApplication.translate
        DialogLog.setWindowTitle(_translate("DialogLog", "Log Setup"))
        self.label.setText(_translate("DialogLog", "dzq"))

