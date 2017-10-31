# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowsHelpView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidgetHelp(object):
    def setupUi(self, TabWidgetHelp):
        TabWidgetHelp.setObjectName("TabWidgetHelp")
        TabWidgetHelp.resize(400, 300)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushOk = QtWidgets.QPushButton(self.tab)
        self.pushOk.setObjectName("pushOk")
        self.gridLayout_2.addWidget(self.pushOk, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        TabWidgetHelp.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidgetHelp.addTab(self.tab1, "")

        self.retranslateUi(TabWidgetHelp)
        QtCore.QMetaObject.connectSlotsByName(TabWidgetHelp)

    def retranslateUi(self, TabWidgetHelp):
        _translate = QtCore.QCoreApplication.translate
        TabWidgetHelp.setWindowTitle(_translate("TabWidgetHelp", "TabWidget"))
        self.pushOk.setText(_translate("TabWidgetHelp", "Ok"))
        self.label.setText(_translate("TabWidgetHelp", "Release :"))
        self.lineEdit.setPlaceholderText(_translate("TabWidgetHelp", "Number Version"))
        self.label_2.setText(_translate("TabWidgetHelp", "Icons :"))
        self.label_4.setText(_translate("TabWidgetHelp", "url icon"))
        self.label_3.setText(_translate("TabWidgetHelp", "Website :"))
        self.label_5.setText(_translate("TabWidgetHelp", "url website"))
        TabWidgetHelp.setTabText(TabWidgetHelp.indexOf(self.tab), _translate("TabWidgetHelp", "Tab 1"))
        TabWidgetHelp.setTabText(TabWidgetHelp.indexOf(self.tab1), _translate("TabWidgetHelp", "Tab 2"))

