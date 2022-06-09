from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog


class AddProj(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('AddProj.ui', self)
        self.setWindowTitle("Project Comparator - создание проекта")

        self.AddEmployee1.clicked.connect(self.add1)
        self.AddEmployee2.clicked.connect(self.add2)
        self.AddEmployee3.clicked.connect(self.add3)
        self.OpenEmployeeList.clicked.connect(self.openlist)

        self.employees = {"category 1": [],
                          "category 2": [],
                          "category 3": []}

    def add1(self):
        self.employees["category 1"].append(self.EmpName1.text())

    def add2(self):
        self.employees["category 2"].append(self.EmpName2.text())

    def add3(self):
        self.employees["category 3"].append(self.EmpName3.text())

    def openlist(self):
        pass

