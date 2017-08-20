import os, json

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, qApp, QLabel, QWidget, QFrame, \
    QGroupBox, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

from BatchLightUE4.Views.WindowsSetup import PathPopup

def show_file_bar(self):
    '''A simple function the generate the File Menu Bar, this attribute has
    a Qt object, the Windows.'''
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
    controlAct = QAction('Control Version', self)
    controlAct.setStatusTip('Activate setup Control Version')
    fileSetup.addAction(controlAct)

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

    return

def show_levels(self):
    '''This function show all levels if he can it.
    She need a Windows Attribute.'''

    path_json_setup = os.path.abspath("BatchLightUE4/Models/setup.json")
    path_json_lvl = os.path.abspath("BatchLightUE4/Models/lvls_tree.json")
    info_text = 'No level(s), setup yours paths.'
    if os.path.isfile(path_json_setup):
        info_text = 'All level(s)'

    lbl = QLabel(info_text, self)
    check = QtWidgets.QCheckBox('Test', self)

    lvl_frm = QtWidgets.QVBoxLayout()
    lvl_frm.addWidget(lbl)
    lvl_frm.addStretch()
    lvl_frm.addWidget(check)

    self.setLayout(lvl_frm)

    return

def builds_tree_lvls():
    print('!! Builds Levels Tree !!')
    path_json_setup = os.path.abspath("BatchLightUE4/Models/setup.json")
    path_json_lvl = os.path.abspath("BatchLightUE4/Models/lvls_tree.json")

    with open(path_json_setup) as f:
        paths_dict = json.load(f)

    lvls = {}
    path_project = os.path.dirname(paths_dict['UE4 Project']) + '/Content/'

    for root, dirs, files in os.walk(path_project):
        for file in files:
            if file.endswith('.umap'):
                print(os.path.join(root, file))
                lvls[file] = os.path.join(root, file)

        with open(path_json_lvl, 'w') as f:
            json.dump(lvls, f, indent=4)

    debug = lvls

    return debug

class MainWindows(QtWidgets.QWidget):
    '''Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... '''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        print('Launch Main Window')

        main_layout = QVBoxLayout()

        ### Menu Bar
        frm_menu = QFrame(self)
        frm_menu.setStyleSheet('background: red')
        main_layout.addWidget(frm_menu)

        ### List Level
        frm_list_lvl = QFrame(self)
        frm_list_lvl.setStyleSheet('background: green')
        main_layout.addWidget(frm_list_lvl)

        ### ----------------------------------------------
        ### Build
        frm_btn_build = QFrame(self)
        frm_btn_build.setStyleSheet('background: blue')

        btn_build = QPushButton('Build')
        btn_cancel = QPushButton('Cancel')

        main_layout.addWidget(frm_btn_build)

        ### Status Bar
        frm_bar = QFrame(self)
        frm_bar.setStyleSheet('background: orange')
        main_layout.addWidget(frm_bar)


        self.setLayout(main_layout)


    # Event
    def menuPath(self):
        self.popupPath = PathPopup()
        self.popupPath.show()

    def buildProcess(self):
        print('Launch Build')

# if __name__ == '__main__':
#     app = QtWidgets.QApplication([])
#     gui = MainWindows()
#     gui.show()
#     app.exec_()
