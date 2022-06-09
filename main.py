from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import uic
import sys

from AddProj import AddProj


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle("Project Comparator")
        self.AddProj.clicked.connect(self.create_add_project)

    def create_add_project(self):
        self.addp = AddProj()
        self.addp.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
