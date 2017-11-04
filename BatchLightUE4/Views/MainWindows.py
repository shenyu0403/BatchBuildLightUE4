import os
import perforce

from os.path import join, isdir, expanduser
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QMessageBox, QFileDialog

from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidgetProjects
from BatchLightUE4.Views.WindowsHelpView import Ui_TabWidgetHelp
from BatchLightUE4.Models.Database import TableProgram
from BatchLightUE4.Controllers.Perfoce import \
    p4_checkout, p4_submit
from BatchLightUE4.Controllers.Project import project_name
from BatchLightUE4.Controllers.Setup import Setup
from BatchLightUE4.Controllers.Swarm import build, swarm_setup

# TODO Add a check if an UE version has launch


class SetupHelp(QtWidgets.QTabWidget, Ui_TabWidgetHelp):
    """This widget contains all help tab"""
    def __init__(self):
        super(SetupHelp, self).__init__()
        self.setupUi(self)
        # self.setWindowTitle('Tab Help')
        #
        print('Windows Help Show')


class SetupTab(QtWidgets.QTabWidget, Ui_TabWidgetProjects):
    """This widget contains all setup tab"""
    def __init__(self):
        super(SetupTab, self).__init__()
        self.setupUi(self)

        self.data = Setup()
        self.job = self.data.last_job_run()

        if self.job:
            # Project Tab
            self.data = TableProgram()
            data_paths = self.data.select_path(1)

            self.ue4_path = data_paths[0][1]
            self.ue4_project = data_paths[0][2]
            self.dir_project = os.path.dirname(self.ue4_project)
            self.scene = data_paths[0][3]
            self.levels_path = join(self.dir_project,
                                    'content', self.scene)
            self.levels_path = os.path.abspath(self.levels_path)
            self.data_level = self.project_list_level(self.levels_path)

            # CSV Tab
            self.data_csv = self.data.csv_data()
            if self.data_csv[0] == 'False' or self.data_csv is None:
                self.csv_boolean = 0
                self.csv_software = 2
            else:
                self.csv_boolean = 2
                self.csv_software = self.data_csv[0]

        else:
            news_DB = True
            self.ue4_path = self.data.base('editor')
            self.ue4_project = self.data.base('project')
            self.scene = self.data.base('sub folder')
            self.data_level = []
            self.csv_boolean = 0
            self.csv_software = 1

        # Project Panel
        self.levels_list = QtGui.QStandardItemModel()
        self.project_tree_generate(self.levels_list, self.data_level)
        self.treeViewLevels.setModel(self.levels_list)
        self.treeViewLevels.clicked.connect(self.project_update_level)
        self.levels_list.setHorizontalHeaderLabels([self.tr('Level Name')])
        self.pushPathOpenUnreal.clicked.connect(lambda: self.open_save(1))
        self.lineEditUnreal.setText(self.ue4_path)
        self.pushPathOpenProject.clicked.connect(lambda: self.open_save(2))
        self.lineEditProject.setText(self.ue4_project)
        name = project_name(self.lineEditProject.text())
        self.lineEditProjectName.setText(name)
        self.lineEditSubfolder.setText(self.scene)

        # Network Panel
        # TODO Make all network options

        # CSV Panel
        """All option about the CSV options."""
        self.csv_checkBox_enable.setCheckState(self.csv_boolean)
        self.csv_checkBox_enable.clicked.connect(self.csv_enable)
        if self.csv_software:
            self.csv_comboBox.itemText(2)

        # Button Box, Save and Cancel
        btn = QtWidgets.QDialogButtonBox
        #   Restore Default

        #   Save
        self.buttonBoxProjects.button(btn.Save).clicked.connect(self.tab_save)
        self.buttonBoxCSV.button(btn.Save).clicked.connect(self.tab_save)

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

        name = project_name(self.lineEditProject.text())
        # self.lineEditProjectName.update()
        self.lineEditProjectName.setText(name)
        self.lineEditProjectName.update()

    def tab_save(self):
        # TODO Update the GUI to show all selected levels
        tab = self.tabBar()
        tab = tab.currentIndex()
        setting = Setup()

        if tab == 1:
            print('Save Network')
        else:
            # Save projects Dataa
            editor = self.lineEditUnreal.text()
            project = self.lineEditProject.text()
            scene = self.lineEditSubfolder.text()

            if not setting.last_job_run():
                self.data_base_save()
            self.data = TableProgram()
            self.data.write_data_path(editor, project, scene)
            self.data.write_data_levels()

            # Save State Data
            csv_state = self.csv_checkBox_enable
            csv_item = 'False'
            if QtWidgets.QAbstractButton.isChecked(csv_state):
                csv_item = self.csv_comboBox.currentText()

            self.data.csv_data(csv_item)

        SetupTab.close(self)

    def data_base_save(self):
        options = QFileDialog.Options()
        directory = join(expanduser('~'), 'BBLUE4')
        database = QFileDialog.getSaveFileName(self,
                                               'Save your projects',
                                               directory=directory,
                                               filter='*.db',
                                               options=options)
        edit = Setup()
        edit.last_job_add(database[0])

    def project_tree_generate(self, parent, elements):
        self.data = TableProgram()
        levels = self.data.select_levels()
        state = i = 0

        for name, path in elements:
            item = QtGui.QStandardItem(name)
            item.setCheckable(True)
            if levels is not None:
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
            absolute_path = join(folder_directory, item)
            child = isdir(absolute_path)
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
    """Main Window, principal view, this windows can show all level,
    access on many option -path setup, network, log... """

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        # Setup settings base

        self.data = Setup()
        self.job = self.data.last_job_run()
        self.checkBoxLevels = {}

        # Triggered Menu
        #     File Menu
        self.actionLast_project.triggered.connect(self.open_save)
        self.actionExit.triggered.connect(self.close)

        #    Setup and Option Menu
        self.actionOptions.triggered.connect(self.view_project)
        self.actionProject.triggered.connect(lambda: self.view_project(0))
        self.actionNetworks.triggered.connect(lambda: self.view_project(1))
        self.actionCSV.triggered.connect(lambda: self.view_project(2))

        #   Help Tab
        self.actionAbout.triggered.connect(lambda: self.view_help(0))
        self.actionShortcut.triggered.connect(lambda: self.view_help(1))

        self.pushLevelsSelect.clicked.connect(lambda: self.select_level(True))
        self.pushLevelsDeselect.clicked.connect(self.select_level)
        self.toolLevelsEdit.clicked.connect(lambda: self.view_project(0))

        # Generate all Checkbox Levels.
        if self.job:
            self.data = TableProgram()
            levels = self.data.select_levels()
            level = self.data.select_levels(state=2)
            csv = self.data.csv_data()
            i = 0
            while i < len(level):
                key = level[i][1]
                self.checkBoxLevels[key] = QtWidgets.QCheckBox(key)
                self.checkBoxLevels[key].setObjectName(key)
                for level_name in levels:
                    if level_name[1] == key and csv[0] is not None:
                        p4 = perforce.connect()
                        path = level_name[2]
                        filename = perforce.Revision(p4, path)
                        other_use = filename._p4dict

                        if hasattr(other_use, 'otherOpen'):
                            bubble_msg = other_use.get('otherOpen0')
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
        # TODO Proof of concept, no object has setup
        if state == 1:
            self.str_debug = 'First Value'
            self.file_setup = filter="Project (*.blight)"
        else:
            self.str_debug = 'Pas de status, basique way'
            self.file_setup = filter="Project (*.blight)"

        (filename, filter) = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open a previous project',
            self.file_setup)

    @staticmethod
    def view_project(index):
        dialog = SetupTab()
        dialog.show()
        dialog.setCurrentIndex(index)

    @staticmethod
    def view_help(index):
        dialog = SetupHelp()
        dialog.show()
        dialog.setCurrentIndex(index)

    # Events
    def select_level(self, state):
        boolean = False
        if state:
            boolean = 2

        data = self.checkBoxLevels
        for key, value in data.items():
            btn = self.checkBoxLevels[key]
            if QtWidgets.QAbstractButton.isEnabled(btn):
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
                cl = p4_checkout(level_rendering[i])
                build(level_rendering[i])
                submit = self.checkBoxSubmit
                if QtWidgets.QAbstractButton.isChecked(submit):
                    p4_submit(cl)
                i += 1

            nbr = len(level_rendering)
            swarm_setup(False)
            msg = 'Rendering Complete, ' + str(nbr) + ' level(s) build.'
            self.statusbar.showMessage(msg)

        else:
            msg = 'Rendering abort.'
            self.statusbar.showMessage(msg)
