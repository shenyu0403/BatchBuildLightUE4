# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsSetupView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PathSetup(object):
    def setupUi(self, PathSetup):
        PathSetup.setObjectName("PathSetup")
        PathSetup.resize(467, 155)
        self.gridLayout = QtWidgets.QGridLayout(PathSetup)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PathSetup)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(PathSetup)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(PathSetup)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(PathSetup)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(PathSetup)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(PathSetup)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PathSetup)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)

        self.retranslateUi(PathSetup)
        self.buttonBox.accepted.connect(PathSetup.accept)
        self.buttonBox.rejected.connect(PathSetup.reject)
        QtCore.QMetaObject.connectSlotsByName(PathSetup)

    def retranslateUi(self, PathSetup):
        _translate = QtCore.QCoreApplication.translate
        PathSetup.setWindowTitle(_translate("PathSetup", "Dialog"))
        self.label.setText(_translate("PathSetup", "Unreal Engine Path :"))
        self.label_2.setText(_translate("PathSetup", "Project File Path :"))
        self.label_3.setText(_translate("PathSetup", "Other Fields :"))

