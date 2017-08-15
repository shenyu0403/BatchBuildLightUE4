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

        # All Bar Menu Top
        # File | Setup | Log | About

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        clearAct = QAction('New', self)
        fileMenu.addAction(clearAct)
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Close this application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        fileSetup = menubar.addMenu('Setup')
        pathAct = QAction('Configure Path', self)
        pathAct.setStatusTip('Setup all paths needed')
        pathAct.triggered.connect(self.menuPath)
        fileSetup.addAction(pathAct)
        networkAct = QAction('Network', self)
        networkAct.setStatusTip('Setup all machine used with your network')
        fileSetup.addAction(networkAct)

        fileLog = menubar.addMenu('Log')
        cleanlogAct = QAction('Clean Log', self)
        cleanlogAct.setStatusTip('Remove your cache files')
        fileLog.addAction(cleanlogAct)

        fileHelp = menubar.addMenu('Help')
        aboutAct = QAction('About', self)
        aboutAct.setStatusTip('Show more information abouts this program')
        fileHelp.addAction(aboutAct)
        updateAct = QAction('Update', self)
        updateAct.setStatusTip('Check the last update')
        fileHelp.addAction(updateAct)
        shortcutAct = QAction('Show Shortcut', self)
        shortcutAct.setStatusTip('View and Setup all Shortcut')
        fileHelp.addAction(shortcutAct)

        # Corps Tools
        # Listing all levels by project
        # Add a many tools, Select All, Unselect...

        lvl_label = QtWidgets.QLabel('All Levels !',self).move(20, 20)
        lvl_tool = QtWidgets.QLabel('Select Tool', self).move(20, 40)
        lvl_build = QtWidgets.QLabel('Build Level(s)', self).move(20, 60)

        btn_ok = QtWidgets.QPushButton('Ok', self).move(40, 90)
        btn_Cancel = QtWidgets.QPushButton('Cancel', self).move(40, 120)

        tip = QtWidgets.QLabel('Don''t forget to update your '
                                     'repository', self)
        tip.move(20, 160)

        self.statusBar()


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
