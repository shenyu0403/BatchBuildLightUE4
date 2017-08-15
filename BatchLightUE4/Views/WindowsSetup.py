from PyQt5 import QtWidgets


class Popup(QtWidgets.QMainWindow):
    '''Call a basic new windows, popup use for all File Menu 'Setup',
    configure Path and Network.'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('Setup yours Path')


class PathPopup(Popup):
    def __init__(self):
        super().__init__()

        self.WindowsPath()


    def WindowsPath(self):
        QtWidgets.QLabel('Hello, is it me you\'re looking for?', self)

