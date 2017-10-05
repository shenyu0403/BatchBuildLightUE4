import json
import os

from PyQt5 import QtWidgets, QtGui

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget
from BatchLightUE4.Models.projects import TableProgram


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidget):
    """This widget contains all setup tab"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tab Setup')

        db_file = os.path.abspath("projects.db")
        if os.path.isfile(db_file):
            data = TableProgram().select_path(0)
            ue4_path = data[0][1]
            ue4_project = data[0][2]

        else:
            ue4_path = ''
            ue4_project = ''

        # Options Panel
        self.listLevels = self.treeViewLevels
        self.algoTreeView.currentIndexChanged.connect(self.tree_generate)

        # listLevels = self.treeViewLevels
        # model = listLevels.model()
        # model.itemChanged.connect(self.generateFinalTree)

        # Path Panel
        # Index >> 1
        self.pushPathOpenUnreal.clicked.connect(lambda: self.open_save(1))
        self.lineEditUnreal.setText(ue4_path)
        self.pushPathOpenProject.clicked.connect(lambda: self.open_save(2))
        self.lineEditProject.setText(ue4_project)

        # Ribbon Default, Save and Cancel
        btn = QtWidgets.QDialogButtonBox
        #   Restore Default

        #   Save
        self.buttonBoxPath.button(btn.Save).clicked.connect(self.tab_save)

        #   Close Event
        self.buttonBoxOptions.button(btn.Cancel).clicked.connect(self.close)
        self.buttonBoxPath.button(btn.Cancel).clicked.connect(self.close)
        self.buttonBoxNetwork.button(btn.Cancel).clicked.connect(self.close)
        self.buttonBoxCSV.button(btn.Cancel).clicked.connect(self.close)

    def open_save(self, state):
        file_description = ''
        file_select = ''

        if state == 1:
            file_description = 'Open the UE4 Editor'
            file_select = 'UE4Editor.exe'

        elif state == 2:
            file_description = 'Open a Unreal Project File'
            file_select = '*.uproject'

        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            file_description,
            filter=file_select)

        if state == 1:
            self.lineEditUnreal.setText(filename)

        elif state == 2:
            self.lineEditProject.setText(filename)

    def tab_save(self):
        editor = self.lineEditUnreal.text()
        project = self.lineEditProject.text()

        TableProgram().write_data_path(editor, project)
        TableProgram().write_data_levels()

        self.checkBoxLevels.update()

        SetupTab.close(self)

    def tree_generate(self):
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

    @staticmethod
    def generate_final_tree():
        print('Add number >> ')

        lvl_final = {}
        lvl_final[0] = "path normalement"

        json_path = os.path.abspath(
            "BatchLightUE4/Models/lvls_tree_final.json")
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
        self.actionLast_project.triggered.connect(self.open_save)
        self.actionExit.triggered.connect(self.closeEvent)

        #    Setup and Option Menu
        self.actionOptions.triggered.connect(self.edit_levels)
        self.actionPaths.triggered.connect(lambda: self.edit_levels(1))
        self.actionNetworks.triggered.connect(lambda: self.edit_levels(2))
        self.actionCSV.triggered.connect(lambda: self.edit_levels(3))

        self.pushLevelsSelect.clicked.connect(lambda: self.select_level(True))
        self.pushLevelsDeselect.clicked.connect(self.select_level)
        self.toolLevelsEdit.clicked.connect(lambda: self.edit_levels(0))

        # CheckBox
        db_file = os.path.abspath("projects.db")
        if os.path.isfile(db_file):
            data = TableProgram().select_levels(0)
            i = 1
            while i < len(data):
                key = data[i][2]
                self.checkBoxLevels[key] = QtWidgets.QCheckBox(key)
                self.checkBoxLevels[key].setObjectName(key)
                self.allLevelsCheck.addWidget(self.checkBoxLevels[key])
                self.allLevelsCheck.contentsMargins()

                i = i + 1

        self.pushToolsBuils.clicked.connect(self.build_level)

    # File Menu
    def open_save(self, state):
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
    def edit_levels(self, id):
        self.dialog = SetupTab()
        self.dialog.show()
        self.dialog.setCurrentIndex(id)

    def select_level(self, state):
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

    def build_level(self):
        print('Build your level(s).')

        TableProgram().debug_data()

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
