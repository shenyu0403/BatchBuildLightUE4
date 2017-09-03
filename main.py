import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

from BatchLightUE4.Views.MainWindows import MainWindows
# from BatchLightUE4.Views.GUI import UIBuildMap

app_info = 'Build Light Batch'

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindows()
    app.setWindowIcon(QtGui.QIcon('BatchLightUE4/Ressources/blacksheep.ico'))
    # w.setGeometry(400, 300, 400, 800)
    w.setWindowTitle(app_info)
    w.show()

    sys.exit(app.exec_())
