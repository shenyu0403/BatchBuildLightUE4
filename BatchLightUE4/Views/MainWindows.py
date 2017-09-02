from PyQt5 import QtWidgets

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

    # Events
    def closeEvent(self, event):
        confirmation = "Are your sur to close this application ?"
        answer = QtWidgets.QMessageBox.question(self, "Confirmation",
                                                confirmation,
                                                QtWidgets.QMessageBox.Yes,
                                                QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()
