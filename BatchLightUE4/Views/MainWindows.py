import os
import perforce

from os import path
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidget
from BatchLightUE4.Models.projects import TableProgram

from ..Controllers.Swarm import build, swarm_setup
from ..Controllers.Perfoce import perforce_checkout, perforce_submit

# TODO Add a check if an UE version has launch


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidget):
    """This widget contains all setup tab"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tab Setup')
        self.data = TableProgram()

        # Generate all data with the Data Base
        db_file = os.path.abspath("projects.db")
        if os.path.isfile(db_file):
            data_paths = self.data.select_path(1)

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
                self.data_level = self.project_list_level(self.levels_path)

        else:
            self.ue4_path = self.ue4_project = self.scene = ''
            self.data_level = []

        # Options Panel
        self.levels_list = QtGui.QStandardItemModel()
        self.project_tree_generate(self.levels_list, self.data_level)
        self.treeViewLevels.setModel(self.levels_list)
        self.treeViewLevels.clicked.connect(self.project_update_level)

        self.levels_list.setHorizontalHeaderLabels([self.tr('Level Name')])

        # Projects Panel
        self.pushPathOpenUnreal.clicked.connect(lambda: self.open_save(1))
        self.lineEditUnreal.setText(self.ue4_path)
        self.pushPathOpenProject.clicked.connect(lambda: self.open_save(2))
        self.lineEditProject.setText(self.ue4_project)
        self.lineEditSubfolder.setText(self.scene)

        # Network Panel
        # TODO Make all network options

        # CSV Panel
        """All option about the CSV options."""

        self.csv_checkBox_enable.clicked.connect(self.csv_enable)

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
        # TODO Update the GUI to show all selected levels
        editor = self.lineEditUnreal.text()
        project = self.lineEditProject.text()
        scene = self.lineEditSubfolder.text()

        self.data.write_data_path(editor, project, scene)
        self.data.write_data_levels()

        SetupTab.close(self)

    def project_tree_generate(self, parent, elements):
        levels = self.data.select_levels()
        state = i = 0

        for name, path in elements:
            item = QtGui.QStandardItem(name)
            item.setCheckable(True)
            if levels is not None:
                print('Nbr entry > ', len(levels), ' | Increment > ', i)
                for i in range(0, len(levels)):
                    if name in levels[i]:
                        state = levels[i][3]
                    i = i + 1

            item.setCheckState(state)
            parent.appendRow(item)
            if path:
                self.project_tree_generate(item, path)

    def project_list_level(self, folder_directory):
        levels = []
        for item in os.listdir(folder_directory):
            absolute_path = path.join(folder_directory, item)
            child = path.isdir(absolute_path)
            if child:
                sublevel = [(item, self.project_list_level(absolute_path))]
                levels.extend(sublevel)
            else:
                if '.umap' in item:
                    sublevel = [(item, [])]
                    levels.extend(sublevel)

        return levels

    def project_update_level(self, index):
        self.data.write_data_levels(treeview=self, index=index)

    def csv_enable(self):
        csv_enable = self.csv_checkBox_enable
        if QtWidgets.QAbstractButton.isChecked(csv_enable):
            self.csv_label_name.setEnabled(True)
            self.csv_comboBox.setEnabled(True)
            self.csv_label_file.setEnabled(True)
            self.csv_lineEdit_file.setEnabled(True)
            self.csv_pushButton_file.setEnabled(True)
            # self.csv_label_id.setEnabled(True)
            # self.csv_lineEdit_id.setEnabled(True)
            # self.csv_label_password.setEnabled(True)
            # self.csv_lineEdit_password.setEnabled(True)

            # Enable inside the DB.

        else:
            self.csv_label_name.setEnabled(False)
            self.csv_comboBox.setEnabled(False)
            self.csv_label_file.setEnabled(False)
            self.csv_lineEdit_file.setEnabled(False)
            self.csv_pushButton_file.setEnabled(False)
            # self.csv_label_id.setEnabled(False)
            # self.csv_lineEdit_id.setEnabled(False)
            # self.csv_label_password.setEnabled(False)
            # self.csv_lineEdit_password.setEnabled(False)


class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main Windows, principal view, this windows can show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

        self.checkBoxLevels = {}
        self.data = TableProgram()

        # Triggered Menu
        #     File Menu
        self.actionLast_project.triggered.connect(self.open_save)
        self.actionExit.triggered.connect(self.close)

        #    Setup and Option Menu
        self.actionOptions.triggered.connect(self.edit_levels)
        self.actionPaths.triggered.connect(lambda: self.edit_levels(1))
        self.actionNetworks.triggered.connect(lambda: self.edit_levels(2))
        self.actionCSV.triggered.connect(lambda: self.edit_levels(3))

        self.pushLevelsSelect.clicked.connect(lambda: self.select_level(True))
        self.pushLevelsDeselect.clicked.connect(self.select_level)
        self.toolLevelsEdit.clicked.connect(lambda: self.edit_levels(0))

        # Enable CSV options
        csv = None
        if csv is not None:
            p4 = perforce.connect()
        # Generate all Checkbox Levels.
        db_file = os.path.abspath("projects.db")
        levels = self.data.select_levels()

        if os.path.isfile(db_file):
            level = self.data.select_levels(state=2)
            i = 0
            while i < len(level):
                key = level[i][1]
                self.checkBoxLevels[key] = QtWidgets.QCheckBox(key)
                self.checkBoxLevels[key].setObjectName(key)
                for level_name in levels:
                    if level_name[1] == key and csv is not None:
                        path = level_name[2]
                        filename = perforce.Revision(p4, path)
                        other_use = filename._p4dict
                        open_by = other_use.get('otherOpen')

                        if open_by is not None:
                            bubble_msg = other_use.get('otherOpen0')
                            print(bubble_msg)
                            tooltip = bubble_msg
                            self.checkBoxLevels[key].setToolTip(tooltip)
                            self.checkBoxLevels[key].setEnabled(False)
                self.allLevelsCheck.addWidget(self.checkBoxLevels[key])
                self.allLevelsCheck.contentsMargins()
                i = i + 1

        self.pushToolsBuils.clicked.connect(self.build_level)
        self.pushToolsBuils.setToolTip(self.pushToolsBuils.statusTip())

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
        boolean = False
        if state:
            boolean = 2

        data = self.checkBoxLevels
        for key, value in data.items():
            btn = self.checkBoxLevels[key]
            btn.setCheckState(boolean)

    def build_level(self):
        # TODO Split the rendering process on a another thread.
        # TODO Add the perfoce base integration
        level_rendering = []
        text = ''

        for key, value in self.checkBoxLevels.items():
            btn = self.checkBoxLevels[key]
            if QtWidgets.QAbstractButton.isChecked(btn):
                level_rendering.append(key)
                nbr = len(level_rendering)
                text = 'Build '
                text = text + str(nbr) + ' level(s).'
            elif len(level_rendering) == 0:
                text = 'No level selected.'

        reply = QMessageBox.question(self, 'Rendering', text)
        level_rendering.sort()

        if reply == QMessageBox.Yes:
            machines = self.checkBoxMachines
            swarm_setup(QtWidgets.QAbstractButton.isChecked(machines))

            for i in range(len(level_rendering)):
                cl = perforce_checkout(level_rendering[i])
                build(level_rendering[i])
                submit = self.checkBoxSubmit
                if QtWidgets.QAbstractButton.isChecked(submit):
                    perforce_submit(cl)
                i = i + 1

            nbr = len(level_rendering)
            swarm_setup(False)
            msg = 'Rendering Complete, ' + str(nbr) + ' level(s) build.'
            self.statusbar.showMessage(msg)

        else:
            msg = 'Rendering abort.'
            self.statusbar.showMessage(msg)

        print(text)
