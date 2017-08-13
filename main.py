import sys
from PyQt5.QtWidgets import QApplication, QWidget

from BatchLightUE4.Views.StatusBar import Example
# from BatchLightUE4.Views.GUI import UIBuildMap

app_info = 'Build Light Batch'

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # w = QWidget()
    # w.resize(450, 150)
    # w.move(300, 300)
    # w.setWindowTitle(app_info)
    # w.show()

    w = Example()

    sys.exit(app.exec_())