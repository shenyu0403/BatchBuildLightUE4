# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrameLevels.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(357, 316)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("BatchLightUE4/Ressources/package.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_grp_lvl = QtWidgets.QLabel(Frame)
        self.label_grp_lvl.setObjectName("label_grp_lvl")
        self.horizontalLayout.addWidget(self.label_grp_lvl)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.name_lvl = QtWidgets.QCheckBox(Frame)
        self.name_lvl.setObjectName("name_lvl")
        self.verticalLayout.addWidget(self.name_lvl)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_grp_lvl.setText(_translate("Frame", "Group Level Named"))
        self.name_lvl.setText(_translate("Frame", "Name Levels"))

