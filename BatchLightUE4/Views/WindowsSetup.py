import sys
from PyQt5 import QtWidgets


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
        self.UnrealPathLabel = QtWidgets.QLabel('Unreal Engine')
        self.UnrealPathField = QtWidgets.QLineEdit('Choose the UE4 Editor.exe')
        self.UnrealPathOpen = QtWidgets.QPushButton('Open')
        self.UnrealPathOpen.clicked.connect(self.choosePath)

        self.UnrealProjectLabel = QtWidgets.QLabel('Unreal Project')
        self.UnrealProjectField = QtWidgets.QLineEdit()
        self.UnrealProjectOpen = QtWidgets.QPushButton('Open Uproject')

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

    def choosePath(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                     '/home')

        print('Choose path : ', path[0])

        self.UnrealPathField.setText(path[0])

        return



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PathPopup()
    gui.show()
    app.exec_()
