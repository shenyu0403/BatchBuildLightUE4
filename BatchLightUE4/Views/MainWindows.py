import os
import perforce
import psutil

from os.path import join, isdir, expanduser, basename, dirname
from PyQt5 import QtWidgets, QtGui, QtCore

from PyQt5.QtWidgets import QMessageBox, QFileDialog

# Adding all view used
from BatchLightUE4.Views.WindowsMainWindows import Ui_MainWindow
from BatchLightUE4.Views.WindowsSetupView import Ui_TabWidgetProjects
from BatchLightUE4.Views.WindowsHelpView import Ui_Help
from BatchLightUE4.Views.WindowsLogView import Ui_DialogLog
from BatchLightUE4.Views.WindowsRendering import Ui_Rendering

# Adding Data Base utils
from BatchLightUE4.Models.Database import TableProgram

# Adding all Operator used
from BatchLightUE4.Controllers.Perfoce import \
    p4_checkout, p4_submit
from BatchLightUE4.Controllers.Project import project_name
from BatchLightUE4.Controllers.Setup import Setup
from BatchLightUE4.Controllers.Swarm import build, swarm_setup

# TODO Add a check if an UE version has launch


class ThreadRendering(QtCore.QThread):
    def __init__(self, level_rendering):
        """
        This Class use the building operator in a separated thread, without
        this class the program freeze when a built it.

        :param level_rendering: A level list we want build it
        :type level_rendering: list
        """
        QtCore.QThread.__init__(self)
        self.lvl_list = level_rendering

    def __del__(self):
        self.wait()

    def run(self):
        # My Thread :) .
        print('Hello, i am a thread')

        for level in self.lvl_list:
            swarm = build(level)
            while swarm:
                self.sleep(30)
                if swarm.pid in psutil.pids():
                    print('looping 30s | ', swarm.pid)

                else:
                    print('Update progress bar')
                    break

            print('End Looping')


class ViewRendering(QtWidgets.QDialog, Ui_Rendering):
    """Rendering Dialog Box."""

    def __init__(self, parent, lvl_list, csv='False'):
        """lvl_list: list with all level rendering.
        csv: data with the CSV used (booelan or list)"""
        super(ViewRendering, self).__init__(parent)
        self.setupUi(self)

        # TODO Split the rendering process on a another thread.
        # Je setup ma progress bar avec les data de base
        self.progressBar.setMaximum(len(lvl_list))
        self.progressBar.setValue(0)
        btn = QtWidgets.QDialogButtonBox
        self.buttonBox.button(btn.Ok).setEnabled(False)
        self.swarm = ThreadRendering(lvl_list)
        self.swarm.start()

        # i = 0
        # for i in range(len(lvl_list)):
        #     if 'False' not in csv[0]:
        #         cl = p4_checkout(lvl_list[i])
            # swarm = build(lvl_list[i])

            # while True:
            #     line = swarm.stdout.readline()
            #     print('line >> ', line)
            #     if not line:
            #         break
            #     print(line)

            # submit = self.checkBoxSubmit
            # if QtWidgets.QAbstractButton.isChecked(submit):
            #     p4_submit(cl)
            # i += 1

        # self.progress_built(lvl_count)
        # while i < lvl_count:
        #     self.label_lvl_name.setText(lvl_list[i])
        #     if 'False' not in csv[0]:
        #         cl = p4_checkout(lvl_list[i])
        # build(lvl_list[i])
        # i += 1

    def progress_built(self):
        # value = QtCore.pyqtSignal([int], ['ProgressValue'])
        self.progressBar.setValue(self.progress_bar.value()+1)
        print('+1 progress bar')


class LogView(QtWidgets.QDialog, Ui_DialogLog):
    """Log Panel"""
    def __init__(self, parent=None):
        super(LogView, self).__init__(parent)
        self.setupUi(self)

        print('Windows Log Show')


class ViewTabHelp(QtWidgets.QDialog, Ui_Help):
    """This widget contains all help tabs ; information about number
    version, release and licence, and all shortcut inside the program."""
    def __init__(self, parent=None):
        super(ViewTabHelp, self).__init__(parent)
        self.setupUi(self)

        self.data = Setup()

        # Version Panel
        url_octi = self.label_url_octicons
        url_website = self.label_url_website
        url_octi.setText('''<a 
        href='https://octicons.github.com/'>Github's Icons - Octicons</a>''')
        url_website.setText('''<a 
        href='https://github.com/stilobique/BatchBuildLightUE4/'>Github 
        Depot</a>''')

        self.pushButtonClose.clicked.connect(self.close)


class ViewTabSetup(QtWidgets.QTabWidget, Ui_TabWidgetProjects):
    """This widget contains all setup tab"""
    def __init__(self):
        super(ViewTabSetup, self).__init__()
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

        ViewTabSetup.close(self)

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
    def __init__(self, parent=None):
        """
        Main Window, principal view, this windows can show all level,
        access on many option -path setup, network, log...
        """
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
        self.actionProject.triggered.connect(self.view_project)
        self.actionNetworks.triggered.connect(lambda: self.view_project(1))
        self.actionCSV.triggered.connect(lambda: self.view_project(2))

        #   Log Panel
        self.actionShow_log_folder.triggered.connect(self.view_log)
        self.actionClean_Log.triggered.connect(self.view_log)

        #   Help Tab
        self.actionAbout.triggered.connect(self.view_help)
        self.actionShortcut.triggered.connect(lambda: self.view_help(1))

        self.pushLevelsSelect.clicked.connect(lambda: self.select_level(True))
        self.pushLevelsDeselect.clicked.connect(self.select_level)
        self.toolLevelsEdit.clicked.connect(lambda: self.view_project(0))

        # Generate all Checkbox Levels.
        # TODO Refactoring the Check perforce (not OO and fonctional only
        # with Perforce ! Need to be think with Subversion and Git.
        if self.job:
            self.data = TableProgram()
            levels = self.data.select_levels()
            level_checkbox = self.data.select_levels(state=2)
            self.csv = self.data.csv_data()
            i = 0
            while i < len(level_checkbox):
                key = level_checkbox[i][1]
                key_folder = basename(dirname(level_checkbox[i][2]))
                self.checkBoxLevels[key] = QtWidgets.QCheckBox(key)
                self.checkBoxLevels[key].setObjectName(key)
                csv_value = self.csv[0]
                if csv_value != str('False'):
                    # TODO Add a progress bar, the the soft check many levels
                    #  the request can be long.
                    for level_name in levels:
                        if key_folder in level_name[2]:
                            p4 = perforce.connect()
                            filename = perforce.Revision(p4, level_name[2])

                            if 'otherOpen' in filename._p4dict:
                                bubble_msg = filename._p4dict.get('otherOpen0')
                                tooltip = bubble_msg
                                self.checkBoxLevels[key].setToolTip(tooltip)
                                self.checkBoxLevels[key].setEnabled(False)

                self.allLevelsCheck.addWidget(self.checkBoxLevels[key])
                self.allLevelsCheck.contentsMargins()
                i = i + 1

            if 'False' not in self.csv[0]:
                self.checkBoxSubmit.setEnabled(True)

        self.pushToolsBuils.clicked.connect(self.view_rendering)
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
        dialog_setup = ViewTabSetup()
        dialog_setup.show()
        dialog_setup.setCurrentIndex(index)

    def view_log(self):
        dialog_log = LogView(self)
        dialog_log.show()

    def view_help(self, index):
        dialog_help = ViewTabHelp(self)
        dialog_help.show()
        dialog_help.tabWidget.setCurrentIndex(index)

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

    def view_rendering(self):
        lvl_rendering = []
        level_count = 0

        for key, value in self.checkBoxLevels.items():
            btn = self.checkBoxLevels[key]
            if QtWidgets.QAbstractButton.isChecked(btn):
                lvl_rendering.append(key)
                level_count = len(lvl_rendering)

        # Check si je peut faire un build (More than 1 levels selected ?
        # -> Non, abort rendering
        # -> Oui, je lance mon thread et ma progress bar.

        if level_count == 0:
            msg = 'No level(s) selected !'
            QMessageBox.information(self, 'Information', msg)

        else:
            text = 'Launch the rendering ?'
            reply = QMessageBox.question(self, 'Rendering', text)
            lvl_rendering.sort()

            if reply == QMessageBox.Yes:
                machines = self.checkBoxMachines
                swarm_setup(QtWidgets.QAbstractButton.isChecked(machines))

                dialog_render = ViewRendering(self, lvl_rendering, self.csv[0])
                dialog_render.show()

                swarm_setup(False)
                # submit = self.checkBoxSubmit
                # if QtWidgets.QAbstractButton.isChecked(submit):
                #     p4_submit(cl)
                msg = 'Level Build'

            else:
                msg = 'Rendering abort.'

        self.statusbar.showMessage(msg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    app.exec_()
