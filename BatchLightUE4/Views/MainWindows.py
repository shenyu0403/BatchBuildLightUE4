import sys

from PyQt5.QtWidgets import QMainWindow, QAction

class MainWindows(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        print('Hello World')

        # All Bar Menu Top
        # File
        # -- Clear
        # -- Exit
        # Setup
        # -- Path
        # -- Network
        # Log
        # - Clean Log

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        clearAct = QAction('New', self)
        exitAct = QAction('Exit', self)
        fileMenu.addAction(clearAct)
        fileMenu.addAction(exitAct)

        fileSetup = menubar.addMenu('Setup')
        pathAct = QAction('Configure Path', self)
        networkAct = QAction('Network', self)
        fileSetup.addAction(pathAct)
        fileSetup.addAction(networkAct)

        fileLog = menubar.addMenu('Log')
        cleanlogAct = QAction('Clean Log', self)
        fileLog.addAction(cleanlogAct)

        # Corps Tools
        # Listing all levels by project
        # Add a many tools, Select All, Unselect...
        # show the perforce user checkout

        # Footer / Status Bar

    # Event
