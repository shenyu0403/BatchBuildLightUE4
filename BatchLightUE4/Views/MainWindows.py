import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(450, 150)
    w.move(300, 300)
    w.setWindowTitle('Batch Light UE4')
    w.show()

    sys.exit(app.exec_())