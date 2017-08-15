from PyQt5.QtWidgets import QAction, qApp
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from BatchLightUE4.Views.WindowsSetup import PathPopup

class MainWindows(QtWidgets.QMainWindow):
    '''Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... '''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QtWidgets.QGridLayout(self)
        self.setLayout(grid)

        # All Bar Menu Top
        # File (Clear | Exit)
        # Setup (Path | Network)
        # Log (Clean Log)
        # Help (About | Show Shortcut)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        clearAct = QAction('New', self)
        fileMenu.addAction(clearAct)
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        fileSetup = menubar.addMenu('Setup')
        pathAct = QAction('Configure Path', self)
        pathAct.triggered.connect(self.menuPath)
        fileSetup.addAction(pathAct)
        networkAct = QAction('Network', self)
        fileSetup.addAction(networkAct)

        fileLog = menubar.addMenu('Log')
        cleanlogAct = QAction('Clean Log', self)
        fileLog.addAction(cleanlogAct)

        fileHelp = menubar.addMenu('Help')
        aboutAct = QAction('About', self)
        fileHelp.addAction(aboutAct)
        shortcutAct = QAction('Show Shortcut', self)
        fileHelp.addAction(shortcutAct)

        # Corps Tools
        # Listing all levels by project
        # Add a many tools, Select All, Unselect...

        lvl_label = QtWidgets.QLabel('All Levels !',self).move(20, 20)
        lvl_tool = QtWidgets.QLabel('Select Tool', self).move(20, 40)
        lvl_build = QtWidgets.QLabel('Build Level(s)', self).move(20, 60)

        btn_ok = QtWidgets.QPushButton('Ok', self).move(40, 90)
        btn_Cancel = QtWidgets.QPushButton('Cancel', self).move(40, 120)


        # show the perforce user checkout

        # Footer / Status Bar


    # Event
    def menuPath(self):
        self.popupPath = PathPopup()
        self.popupPath.show()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication([])
#     gui = MainWindows()
#     gui.show()
#     app.exec_()
