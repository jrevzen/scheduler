import json
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication, QWidget, QHBoxLayout, QVBoxLayout
from scheduling.MyDate import MyDate
from dnd import DropLabel

class DateWidget(QWidget):

    def __init__(self, week_num=0):
        super().__init__()

        self.initui()

    def initui(self):
        self.setWindowTitle("DateWidget")
        self.date_layout = QHBoxLayout()
        self.dayName = MyDate(1).col_headers
        self.title = QLabel("סידור")
        self.label1 = QLabel("        ")
        self.label1.setFixedSize(70, 25)
        self.date_layout.addWidget(self.label1)

        for i in range(0, len(self.dayName)):
            self.label1 = QLabel(self.dayName[i])
            self.label1.setFixedSize(70, 25)
            self.date_layout.addWidget(self.label1)
        self.setLayout(self.date_layout)



class WeekWidget(QWidget):

    def __init__(self,workers_list):
        super().__init__()
        self.setWindowTitle("WeekShifts")
        self.week_layout = WeekLayout(workers_list)
        self.setLayout(self.week_layout)
        self.title = QLabel("סידור")


class WeekLayout(QGridLayout):

    def initui(self):
        # currentWeek = None
        for j in range(0, len(self.workers_list)):
            self.label1 = QLabel(self.workers_list[j])
            self.label1.setFixedSize(70, 25)
            self.addWidget(self.label1, j + 2, 0)

        for i in range(0, len(self.workers_list)):
            for j in range(0,7):
                self.label2 = DropLabel('')
                self.label2.setFrameShape(QtWidgets.QFrame.Box)
                self.addWidget(self.label2, i + 2, j + 1)

    def __init__(self,workers_list):
        super().__init__()
        self.workers_list = workers_list
        self.initui()


class DateWorkersWidget(QWidget):

    # static method
    with open('scheduling/workers.json') as f:
        data = json.load(f)

    def retrieve_managers(self):
        manager_list = DateWorkersWidget.data["managers"]
        return manager_list

    def retrieve_reception(self):
        reception_list = DateWorkersWidget.data["reception"]
        return reception_list

    def initui(self):
        self.setWindowTitle("DateWidget")
        self.date_work_layout = QVBoxLayout()
        self.dateWidget = DateWidget()
        self.weekWidget0 = WeekWidget(self.retrieve_managers())
        self.weekWidget1 = WeekWidget(self.retrieve_reception())
        self.setLayout(self.date_work_layout)
        self.date_work_layout.addWidget(self.dateWidget)
        self.date_work_layout.addWidget(self.weekWidget0)
        self.date_work_layout.addWidget(self.weekWidget1)

    def __init__(self):

        super().__init__()
        self.dayName = MyDate(1).col_headers
        self.initui()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    week_shifts = DateWorkersWidget()
    week_shifts.show()

    sys.exit(app.exec())
