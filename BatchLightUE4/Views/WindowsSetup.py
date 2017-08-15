import os, sys, json
from PyQt5 import QtWidgets

from ..Models.DB import paths_dict


class Popup(QtWidgets.QWidget):
    '''Call a basic new windows, this popup use for all menu 'Setup',
    configure Path and Network.'''
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('Setup yours Paths')


class PathPopup(Popup):
    def __init__(self):
        super().__init__()

        self.WindowsPath()

    def WindowsPath(self):
        # Define base variable (path empty or not)
        if paths_dict:
            EditorPath = paths_dict["UE4 Editor"]
            ProjectPath = paths_dict["UE4 Project"]
        else:
            EditorPath = 'UE4 Editor'
            ProjectPath = 'uproject File'

        # Setup Unreal Editor Path
        self.UnrealPathLabel = QtWidgets.QLabel('Unreal Engine')
        self.UnrealPathField = QtWidgets.QLineEdit(EditorPath)
        self.UnrealPathOpen = QtWidgets.QPushButton('Open File')
        self.UnrealPathOpen.clicked.connect(lambda :self.choosePath('Editor'))

        # Setup Unreal Project Path
        self.UnrealProjectLabel = QtWidgets.QLabel('Unreal Project')
        self.UnrealProjectField = QtWidgets.QLineEdit(ProjectPath)
        self.UnrealProjectOpen = QtWidgets.QPushButton('Open File')
        self.UnrealProjectOpen.clicked.connect(lambda :self.choosePath(
            'Project'))

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(self.UnrealPathLabel, 1, 0)
        grid.addWidget(self.UnrealPathField, 1, 1)
        grid.addWidget(self.UnrealPathOpen, 1, 2)

        grid.addWidget(self.UnrealProjectLabel, 2, 0)
        grid.addWidget(self.UnrealProjectField, 2, 1)
        grid.addWidget(self.UnrealProjectOpen, 2, 2)

        self.setLayout(grid)

        # self.setGeometry(300, 300, 350, 300)
        self.show()

    def choosePath(self, file):
        if paths_dict:
            if file == 'Editor':
                openpath = paths_dict["UE4 Editor"]
            elif file == 'Project':
                openpath = paths_dict["UE4 Project"]
        else:
            openpath = '/'

        filedialog = QtWidgets.QFileDialog
        path = filedialog.getOpenFileName(self, 'Open file', openpath)
        textfield = ''

        print('Choose path : ', path[0])
        if file == 'Editor':
            paths_dict['UE4 Editor'] = path[0]
            textfield = self.UnrealPathField.setText(path[0])
            print('Save Editor')

        elif file == 'Project':
            paths_dict['UE4 Project'] = path[0]
            print('Save Unreal project')
            textfield = self.UnrealProjectField.setText(path[0])


        path_json = os.path.abspath("BatchLightUE4/Models/setup.json")
        with open(path_json, 'w') as f:
            json.dump(paths_dict, f, indent=4)

        return textfield


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PathPopup()
    gui.show()
    app.exec_()
