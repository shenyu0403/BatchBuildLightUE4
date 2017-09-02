import os, json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, qApp, QLabel, QWidget, \
    QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

from BatchLightUE4.Views.WindowsSetup import PathPopup
from BatchLightUE4.Views.MainWindows import Ui_MainWindow

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


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    '''Main Windows, principal view, this windows can be show all level,
    access on many option -path setup, network, log... '''

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

    def initUI(self):
        print('Launch Main Window')


    # Event
    def buildProcess(self):
        print('Launch Build')
