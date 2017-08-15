import sys
from PyQt5 import QtWidgets, QtGui


class Popup(QtWidgets.QWidget):
    '''Call a basic new windows, this popup use for all menu 'Setup',
    configure Path and Network.'''
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('Setup yours Path')


class PathPopup(Popup):
    def __init__(self):
        super().__init__()

        self.WindowsPath()

    def WindowsPath(self):
        UnrealPathLabel = QtWidgets.QLabel('Unreal Engine')
        UnrealPathField = QtWidgets.QLineEdit()
        UnrealPathOpen = QtWidgets.QPushButton('Open')


        UnrealProjectLabel = QtWidgets.QLabel('Unreal Project')
        UnrealProjectField = QtWidgets.QLineEdit()
        UnrealProjectOpen = QtWidgets.QPushButton('Open Uproject')

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(UnrealPathLabel, 1, 0)
        grid.addWidget(UnrealPathField, 1, 1)
        grid.addWidget(UnrealPathOpen, 1, 2)

        grid.addWidget(UnrealProjectLabel, 2, 0)
        grid.addWidget(UnrealProjectField, 2, 1)
        grid.addWidget(UnrealProjectOpen, 2, 2)

        self.setLayout(grid)

        # self.setGeometry(300, 300, 350, 300)
        self.show()

    def showDialog(self):

        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                      '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PathPopup()
    gui.show()
    app.exec_()
