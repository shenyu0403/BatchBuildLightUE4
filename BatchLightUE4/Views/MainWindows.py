import json
import os

from os import path, walk
from PyQt5 import QtWidgets, QtGui, QtCore

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget
from BatchLightUE4.Models.projects import TableProgram


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidget):
    """This widget contains all setup tab"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tab Setup')

        # self.data_level = [
        #     ('Etienne', [
        #         ('light', []),
        #         ('truc', [])
        #                 ]
        #      ),
        #     ('Roger', [
        #         ('light', []),
        #         ('truc', [])
        #     ]
        #      ),
        #     ('Checker', []
        #      )
        #     ]

        # Generate all data with the Data Base
        db_file = os.path.abspath("projects.db")
        if os.path.isfile(db_file):
            data_paths = TableProgram().select_path(1)

            if data_paths.__len__() == 0:
                self.ue4_path = ''
                self.ue4_project = ''
                self.scene = ''
                self.data_level = []

            else:
                self.ue4_path = data_paths[0][1]
                self.ue4_project = data_paths[0][2]
                self.dir_project = os.path.dirname(self.ue4_project)
                self.scene = data_paths[0][3]
                self.levels_path = path.join(self.dir_project,
                                             'content', self.scene)
                self.levels_path = os.path.abspath(self.levels_path)
                self.data_level = self.list_level(self.levels_path)
                # self.data_level = [
                #     ('Etienne', [
                #         ('light', []),
                #         ('truc', [])
                #     ]
                #      ),
                #     ('Roger', [
                #         ('light', []),
                #         ('truc', [])
                #     ]
                #      ),
                #     ('Checker', []
                #      )
                # ]
                # print(self.data_level)

        else:
            self.ue4_path = self.ue4_project = self.scene = ''
            self.data_level = []

        # Options Panel
        self.levels_list = QtGui.QStandardItemModel()
        self.tree_generate(self.levels_list, self.data_level)
        self.treeViewLevels.setModel(self.levels_list)

        self.levels_list.setHorizontalHeaderLabels([self.tr('Level Name')])

        # Projects Panel
        self.pushPathOpenUnreal.clicked.connect(lambda: self.open_save(1))
        self.lineEditUnreal.setText(self.ue4_path)
        self.pushPathOpenProject.clicked.connect(lambda: self.open_save(2))
        self.lineEditProject.setText(self.ue4_project)
        self.lineEditSubfolder.setText(self.scene)

        # Ribbon Default, Save and Cancel
        btn = QtWidgets.QDialogButtonBox
        #   Restore Default

        #   Save
        self.buttonBoxProjects.button(btn.Save).clicked.connect(self.tab_save)

        #   Close Event
        self.buttonBoxProjects.button(btn.Cancel).clicked.connect(self.close)
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
        # TODO Add an update with the master windows to show all selected
        # levels
        editor = self.lineEditUnreal.text()
        project = self.lineEditProject.text()
        scene = self.lineEditSubfolder.text()

        TableProgram().write_data_path(editor, project, scene)
        # TableProgram().write_data_levels()

        # MainWindows.self.checkBoxLevels.update()

        SetupTab.close(self)

    def tree_generate(self, parent, elements):
        for name, path in elements:
            item = QtGui.QStandardItem(name)
            item.setCheckable(True)
            parent.appendRow(item)
            if path:
                self.tree_generate(item, path)

    def list_level(self, folder_directory):
        levels = []
        for item in os.listdir(folder_directory):
            absolute_path = path.join(folder_directory, item)
            child = path.isdir(absolute_path)
            print(absolute_path)
            print('level >> ', item, ' | Child >> ', child)
            if child:
                sublevel = [(item, self.list_level(absolute_path))]
            else:
                sublevel = [(item, [])]

            levels.extend(sublevel)

        print(levels)

        return levels


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
            data = TableProgram().select_levels()
            i = 1
            while i < len(data):
                key = data[i][1]
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
