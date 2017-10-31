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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(False)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BatchLightUE4/Resources/pin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidgetHelp.addTab(self.tab, icon, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("BatchLightUE4/Resources/text-size.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidgetHelp.addTab(self.tab1, icon1, "")

        self.retranslateUi(TabWidgetHelp)
        TabWidgetHelp.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidgetHelp)

    def retranslateUi(self, TabWidgetHelp):
        _translate = QtCore.QCoreApplication.translate
        TabWidgetHelp.setWindowTitle(_translate("TabWidgetHelp", "TabWidget"))
        self.pushButton.setText(_translate("TabWidgetHelp", "Ok"))
        self.label.setText(_translate("TabWidgetHelp", "Number Version :"))
        self.lineEdit.setPlaceholderText(_translate("TabWidgetHelp", "Release Number"))
        self.label_2.setText(_translate("TabWidgetHelp", "Icons and Ressrouces :"))
        self.label_4.setText(_translate("TabWidgetHelp", "https://octicons.github.com/"))
        self.label_3.setText(_translate("TabWidgetHelp", "Websites"))
        self.label_5.setText(_translate("TabWidgetHelp", "https://github.com/stilobique/BatchBuildLightUE4"))
        TabWidgetHelp.setTabText(TabWidgetHelp.indexOf(self.tab), _translate("TabWidgetHelp", "About and Updates"))
        TabWidgetHelp.setTabText(TabWidgetHelp.indexOf(self.tab1), _translate("TabWidgetHelp", "Shortcut"))

