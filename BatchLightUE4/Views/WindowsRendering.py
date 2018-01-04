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
        Rendering.setWindowModality(QtCore.Qt.WindowModal)
        Rendering.resize(400, 211)
        self.gridLayout = QtWidgets.QGridLayout(Rendering)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Rendering)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Rendering)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)
        self.groupLvlState = QtWidgets.QGroupBox(Rendering)
        self.groupLvlState.setObjectName("groupLvlState")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupLvlState)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lyt_lvl1 = QtWidgets.QHBoxLayout()
        self.lyt_lvl1.setObjectName("lyt_lvl1")
        self.lvl_name1 = QtWidgets.QLabel(self.groupLvlState)
        self.lvl_name1.setToolTip("")
        self.lvl_name1.setStatusTip("")
        self.lvl_name1.setWhatsThis("")
        self.lvl_name1.setAccessibleName("")
        self.lvl_name1.setAccessibleDescription("")
        self.lvl_name1.setText("Level rendering name :")
        self.lvl_name1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lvl_name1.setObjectName("lvl_name1")
        self.lyt_lvl1.addWidget(self.lvl_name1)
        self.lvl_logo1 = QtWidgets.QLabel(self.groupLvlState)
        self.lvl_logo1.setMinimumSize(QtCore.QSize(16, 16))
        self.lvl_logo1.setMaximumSize(QtCore.QSize(16, 16))
        self.lvl_logo1.setText("")
        self.lvl_logo1.setPixmap(QtGui.QPixmap("BatchLightUE4/Resources/s-valid.png"))
        self.lvl_logo1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lvl_logo1.setObjectName("lvl_logo1")
        self.lyt_lvl1.addWidget(self.lvl_logo1)
        self.lvl_state1 = QtWidgets.QLabel(self.groupLvlState)
        self.lvl_state1.setObjectName("lvl_state1")
        self.lyt_lvl1.addWidget(self.lvl_state1)
        self.verticalLayout.addLayout(self.lyt_lvl1)
        self.gridLayout.addWidget(self.groupLvlState, 0, 0, 1, 2)

        self.retranslateUi(Rendering)
        self.buttonBox.accepted.connect(Rendering.accept)
        self.buttonBox.rejected.connect(Rendering.reject)
        QtCore.QMetaObject.connectSlotsByName(Rendering)

    def retranslateUi(self, Rendering):
        _translate = QtCore.QCoreApplication.translate
        Rendering.setWindowTitle(_translate("Rendering", "Rendering State"))
        self.groupLvlState.setTitle(_translate("Rendering", "States building :"))
        self.lvl_state1.setText(_translate("Rendering", "statut levels"))

