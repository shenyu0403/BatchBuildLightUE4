from PyQt5 import QtWidgets

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidget):
    """This object create a new windows"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        # Triggered Menu
        #     File Menu
        self.actionLast_project.triggered.connect(self.openSave)
        self.actionExit.triggered.connect(self.closeEvent)

        #    Setup and Option Menu
        self.actionOptions.triggered.connect(self.editLevels)
        self.actionPaths.triggered.connect(lambda: self.editLevels(1))
        self.actionNetworks.triggered.connect(lambda: self.editLevels(2))
        self.actionCSV.triggered.connect(lambda: self.editLevels(3))

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
    def editLevels(self, id):
        print(id)
        self.dialog = SetupTab()
        self.dialog.show()
        self.dialog.setCurrentIndex(id)

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
