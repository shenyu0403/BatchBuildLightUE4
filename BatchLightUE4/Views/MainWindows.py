from PyQt5 import QtWidgets

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget


class SetupDialog(QtWidgets.QTabWidget, Ui_TabWidget):
    """This object create a new windows"""
    def __init__(self):
        super(SetupDialog, self).__init__()
        self.setupUi(self)


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        self.actionLast_project.triggered.connect(self.openSave)
        self.actionExit.triggered.connect(self.closeEvent)
        self.actionPaths.triggered.connect(self.editLevels)
        self.actionNetworks.triggered.connect(self.editNetwork)

        self.pushLevelsSelect.clicked.connect(lambda: self.selectLevel(True))
        self.pushLevelsDeselect.clicked.connect(self.selectLevel)
        self.toolLevelsEdit.clicked.connect(self.editLevels)

        self.pushToolsBuils.clicked.connect(self.buildLevel)

    # File Menu
    def openSave(self):
        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open a previous project',
            filter="Project (*.blight)")

    # Events
    def editLevels(self):
        self.dialog = SetupDialog()
        self.dialog.show()

    def editNetwork(self):
        popup = Ui_Form()
        popup.setupUi(SetupDialog)
        w = SetupDialog()
        w.show()

    def selectLevel(self, state):
        if state:
            print('Select all Level')

        else:
            print('Deselect all Level')

    def buildLevel(self):
        print('Build Level')

    def closeEvent(self, event):
        confirmation = "Are your sur you want close this application ?"
        answer = QtWidgets.QMessageBox.question(self, "Confirmation",
                                                confirmation,
                                                QtWidgets.QMessageBox.Yes,
                                                QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()
