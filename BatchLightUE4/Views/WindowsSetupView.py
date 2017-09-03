# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsSetupView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(400, 300)
        self.Softwareoptions = QtWidgets.QWidget()
        self.Softwareoptions.setObjectName("Softwareoptions")
        self.gridLayout = QtWidgets.QGridLayout(self.Softwareoptions)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.Softwareoptions)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        TabWidget.addTab(self.Softwareoptions, "")
        self.Path = QtWidgets.QWidget()
        self.Path.setObjectName("Path")
        self.label_2 = QtWidgets.QLabel(self.Path)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        TabWidget.addTab(self.Path, "")
        self.Network = QtWidgets.QWidget()
        self.Network.setObjectName("Network")
        self.label_3 = QtWidgets.QLabel(self.Network)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        TabWidget.addTab(self.Network, "")
        self.CSV = QtWidgets.QWidget()
        self.CSV.setObjectName("CSV")
        self.label_4 = QtWidgets.QLabel(self.CSV)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 47, 13))
        self.label_4.setObjectName("label_4")
        TabWidget.addTab(self.CSV, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.label.setText(_translate("TabWidget", "Options software"))
        TabWidget.setTabText(TabWidget.indexOf(self.Softwareoptions), _translate("TabWidget", "Page"))
        self.label_2.setText(_translate("TabWidget", "All path setup"))
        TabWidget.setTabText(TabWidget.indexOf(self.Path), _translate("TabWidget", "Path"))
        self.label_3.setText(_translate("TabWidget", "Network Setup"))
        TabWidget.setTabText(TabWidget.indexOf(self.Network), _translate("TabWidget", "Network"))
        self.label_4.setText(_translate("TabWidget", "Define your CSV software"))
        TabWidget.setTabText(TabWidget.indexOf(self.CSV), _translate("TabWidget", "CSV"))

