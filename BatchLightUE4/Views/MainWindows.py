import os, json

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QAction, qApp, QLabel, QWidget, QFrame, \
    QGroupBox, QVBoxLayout, QPushButton, QHBoxLayout
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


class MainWindows(QtWidgets.QMainWindow):
    '''Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... '''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        print('Launch Main Window')

        ### Menu Bar
        show_file_bar(self)

        ### Central Widget
            # Definition des differents objects pour le layout Levels,
            # generate a Toolbar and checkbox list
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.lvl_btn_select = QPushButton("Select", self.centralWidget)
        self.lvl_btn_deselect = QPushButton("Deselect", self.centralWidget)
        self.lvl_btn_edit = QPushButton("Edit", self.centralWidget)
        self.lvl_label = QLabel("Level(s)", self.centralWidget)

        self.btn_tools = QLabel("Tools", self.centralWidget)
        self.btn_build = QLabel("Launch Build", self.centralWidget)
        self.btn_log = QLabel("Clear Log", self.centralWidget)

        ## Positionment Central Widget
            # layout Levels
        self.lvl_layout_h = QHBoxLayout()
        self.lvl_layout_h.addWidget(self.lvl_btn_select)
        self.lvl_layout_h.addWidget(self.lvl_btn_deselect)
        self.lvl_layout_h.addWidget(self.lvl_btn_edit)

        self.lvl_layout_v = QVBoxLayout()
        self.lvl_layout_v.addLayout(self.lvl_layout_h)
        self.lvl_layout_v.addWidget(self.lvl_label)

            # Layout Tools
        self.tool_layout = QHBoxLayout()
        self.tool_layout.addWidget(self.btn_build)
        self.tool_layout.addWidget(self.btn_log)

        self.tool_layout_v = QVBoxLayout()
        self.tool_layout_v.addLayout(self.tool_layout)
        self.tool_layout_v.addWidget(self.btn_tools)

        # Merge all layout
        self.all_layout = QVBoxLayout(self.centralWidget)
        self.all_layout.addLayout(self.lvl_layout_v)
        self.all_layout.addLayout(self.tool_layout_v)

        ### Statut Bar
        self.statusBar()


    # Event
    def menuPath(self):
        self.popupPath = PathPopup()
        self.popupPath.show()

    def buildProcess(self):
        print('Launch Build')
