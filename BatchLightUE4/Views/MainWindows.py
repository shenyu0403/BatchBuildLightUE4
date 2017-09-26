import json
import os

from PyQt5 import QtWidgets, QtGui

from BatchLightUE4.Controllers.TreeLevels import builds_tree_lvls
from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidget):
    """This widget contains all setup tab"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tab Setup')

        json_path = os.path.abspath("BatchLightUE4/Models/setup_path.json")
        if os.path.isfile(json_path):
            data = json.loads(open(json_path).read())
            ue4_path = data['UE4 Editor']
            ue4_project = data['UE4 Project']

        else:
            ue4_path = ''
            ue4_project = ''

        # Options Panel
        self.listLevels = self.treeViewLevels
        self.algoTreeView.currentIndexChanged.connect(self.treeGenerate)

        # listLevels = self.treeViewLevels
        # model = listLevels.model()
        # model.itemChanged.connect(self.generateFinalTree)

        BTN = QtWidgets.QDialogButtonBox
        self.buttonBoxOptions.button(BTN.Cancel).clicked.connect(self.close)

        # Path Panel
        # Index >> 1
        self.pushPathOpenUnreal.clicked.connect(lambda: self.openSave(1))
        self.lineEditUnreal.setText(ue4_path)
        self.pushPathOpenProject.clicked.connect(lambda: self.openSave(2))
        self.lineEditProject.setText(ue4_project)
        self.pushPathDataLevels.clicked.connect(builds_tree_lvls)

        BTN = QtWidgets.QDialogButtonBox
        self.buttonBoxPath.button(BTN.Save).clicked.connect(self.tabSave)

    def openSave(self, state):
        if state == 1:
            file_description = 'Open the UE4 Editor'
            file_select = 'UE4Editor.exe'
            field = self.lineEditUnreal.setText

        elif state == 2:
            file_description = 'Open a Unreal Project File'
            file_select = '*.uproject'
            field = self.lineEditProject.setText

        else:
            file_description = 'Open a File'
            file_select = ''
            field = None

        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            file_description,
            filter=file_select)

    def tabSave(self):
        editor = self.lineEditUnreal.text()
        project = self.lineEditProject.text()

        path_dict = {
            "UE4 Editor": editor,
            "UE4 Project": project,
        }

        json_path = os.path.abspath("BatchLightUE4/Models/setup_path.json")
        with open(json_path, 'w') as f:
            json.dump(path_dict, f, indent=4)

        SetupTab.close(self)

    def treeGenerate(self):
        index = self.algoTreeView.currentIndex()

        if index is None:
            index = 0

        print(index)
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['Master Levels', 'Sublevel'])
        self.listLevels.setModel(model)
        self.listLevels.setSortingEnabled(True)
        self.listLevels.setColumnWidth(0, 150)
        it_master = {}
        it_child = {}

        json_tree_lvl = os.path.abspath("BatchLightUE4/Models/lvls_tree.json")
        if os.path.isfile(json_tree_lvl):
            data = json.loads(open(json_tree_lvl).read())
            for key, path in sorted(data.items()):
                folder = os.path.basename(os.path.dirname(path))

                if index == 0:
                    key = key.replace('.umap', '')
                    if folder in key:
                        # Create a master
                        if it_master.get(folder) is None:
                            it_master[folder] = QtGui.QStandardItem(folder)
                            it_master[folder].setCheckable(True)
                            model.appendRow(it_master[folder])
                            it_child[key] = QtGui.QStandardItem(key)
                            it_master[folder].appendRow(it_child[key])
                        else:
                            it_child[key] = QtGui.QStandardItem(key)
                            it_master[folder].appendRow(it_child[key])

                elif index == 1:
                    if 'Master' in key:
                        key = key.replace('.umap', '')
                        key = key.replace('_', ' ')
                        it_master[key] = QtGui.QStandardItem(key)
                        it_master[key].setCheckable(True)
                        model.appendRow(it_master[key])

                    else:
                        it_child[key] = QtGui.QStandardItem(key)
                        show_path = 'Master_' + folder + '.umap'
                        if show_path in it_master:
                            it_master[show_path].appendRow(it_child[key])
                        else:
                            print('Level exclude >> ', key)

                elif index == 2:
                    key = key.replace('.umap', '')
                    if 'Scenes' or 'Levels' in folder:
                        folder = folder.replace('_', ' ')

                        if it_master.get(folder) is None:
                            it_master[folder] = QtGui.QStandardItem(folder)
                            it_master[folder].setCheckable(True)
                            model.appendRow(it_master[folder])
                            it_child[key] = QtGui.QStandardItem(key)
                            it_master[folder].appendRow(it_child[key])
                        else:
                            it_child[key] = QtGui.QStandardItem(key)
                            it_master[folder].appendRow(it_child[key])

    def generateFinalTree(self):
        print('Add number >> ')

        lvl_final = {}
        lvl_final[0] = "path normalement"

        json_path = os.path.abspath("BatchLightUE4/Models/lvls_tree_final.json")
        with open(json_path, 'w') as f:
            json.dump(lvl_final, f, indent=4)


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Windows, principal view, this windows can show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        self.checkBoxLevels = {}

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
        self.toolLevelsEdit.clicked.connect(lambda: self.editLevels(0))

        # CheckBox
        json_tree_lvl = os.path.abspath("BatchLightUE4/Models/lvls_tree.json")
        if os.path.isfile(json_tree_lvl):
            data = json.loads(open(json_tree_lvl).read())

            for key, path in sorted(data.items()):
                self.checkBoxLevels[key] = QtWidgets.QCheckBox(key)
                self.checkBoxLevels[key].setObjectName(key)
                self.allLevelsCheck.addWidget(self.checkBoxLevels[key])
                self.allLevelsCheck.contentsMargins()

        self.pushToolsBuils.clicked.connect(self.buildLevel)

    # File Menu
    def openSave(self, state):
        if state == 1:
            self.str_debug = 'First Value'
            self.file_setup = filter="Project (*.blight)"
        else:
            self.str_debug = 'Pas de status, basique way'
            self.file_setup = filter="Project (*.blight)"


        # print(self.str_debug)

        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open a previous project',
            self.file_setup)

    # Events
    def editLevels(self, id):
        self.dialog = SetupTab()
        self.dialog.show()
        self.dialog.setCurrentIndex(id)

    def selectLevel(self, state):
        if state:
            print('Select all Level')
            boolean = True

        else:
            print('Deselect all Level')
            boolean = False

        json_tree_lvl = os.path.abspath("BatchLightUE4/Models/lvls_tree.json")
        if os.path.isfile(json_tree_lvl):
            data = json.loads(open(json_tree_lvl).read())

            for key, path in data.items():
                self.checkBoxLevels[key].setChecked(boolean)

    def buildLevel(self):
        print('Build Level')

    def closeEvent(self, event):
        confirmation = "Are your sur you want close this application ?"
        answer = QtWidgets.QMessageBox.question(self,
                                                "Confirmation",
                                                confirmation,
                                                QtWidgets.QMessageBox.Yes,
                                                QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()
