import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget, QAction

from Buttons import Buttons, Instructions
from WeekShifts import DateWorkersWidget
from dnd import Drag_Label, Drag_Label_Holiday, Drag_Label_deny
from scheduling import _backend


class WeekShifts_Buttons(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.initui()
        self.constraints = []

    def initui(self):
        pop_message = QAction('הודות', self)
        pop_message.triggered.connect(self.message_box)
        self.menubar = self.menuBar()
        self.menubar.addAction(pop_message)

        self.setWindowTitle("סידור עבודה מח' אחזקה")

        self.date_work_widget = DateWorkersWidget()
        self.instructions = Instructions()
        self.button_click = Buttons()
        self.drag_label = Drag_Label()
        self.drag_label_holiday = Drag_Label_Holiday()
        self.drag_Label_deny = Drag_Label_deny()

        self.main_widget.layout = QGridLayout()
        self.main_widget.layout.addWidget(self.instructions, 0, 0, 2, 1)
        self.main_widget.layout.addWidget(self.drag_label, 2, 0, 1, 1)
        self.main_widget.layout.addWidget(self.drag_label_holiday, 3, 0, 1, 1)
        self.main_widget.layout.addWidget(self.drag_Label_deny, 4, 0, 1, 1)
        self.main_widget.layout.addWidget(self.button_click, 5, 0, 1, 1)
        self.main_widget.layout.addWidget(self.date_work_widget, 0, 1, 6, 2)

        self.button_click.button_load.clicked.connect(self.load_sheet)
        self.button_click.button_compute.clicked.connect(self.load_sheet_and_compute)
        self.button_click.button_save.clicked.connect(self.save_sheet)
        self.button_click.button_reset.clicked.connect(self.load_blank)
        self.main_widget.setLayout(self.main_widget.layout)

        self.setCentralWidget(self.main_widget)

    def message_box(self):
        _backend.message_box()

    def load_sheet(self):
        _backend.load_sheet(self)

    def load_sheet_and_compute(self):
        _backend.load_sheet_and_compute(self)

    def save_sheet(self):
        _backend.save_sheet(self)

    def load_blank(self):
        _backend.load_blank(self)


    def compute_date(self):
        _backend.compute_date(self)

    def handlePreview(self):
        _backend.handlePreview(self)

    def collect_weekend_constraints(self):
        """ Collect constraints from last weeks schedule
        """
        table = self.date_work_widget.shiftWidget
        for row in range(1, table.week_layout.rowCount() - 1):
            item = table.itemAtPosition(row,6)
            if item.widget().text() == '20-07':
                self.constraints.append((row - 1, 0, 0, -2))
            elif item.widget().text() == '07-20':
                self.constraints.append((row - 1, 0, 0, -2))
            # print(''.join(str(self.constraints)))

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        Print_Widget = self.week_shifts
        cursor = QtGui.QTextFrame(Print_Widget)
        table = cursor.insertTable(
            self.table.rowCount(), self.table.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.table.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    week_shifts_buttons = WeekShifts_Buttons()
    week_shifts_buttons.update()
    week_shifts_buttons.show()
    sys.exit(app.exec())


