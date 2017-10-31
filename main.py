import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from BatchLightUE4.Views.MainWindows import MainWindows

app_info = 'B-BlUE4'

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindows()
    app.setWindowIcon(QtGui.QIcon('BatchLightUE4/Resources/light-bulb.png'))
    w.setWindowTitle(app_info)
    w.show()

    sys.exit(app.exec_())
