import csv
import os

from PyQt5 import QtPrintSupport
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from scheduling.MyDate import MyDate
from scheduling.shift_scheduling_sat0 import solve_shift_scheduling
# from WeekShiftsButtons import WeekShifts_Buttons


def constriant_box(info):
    msgbox = QMessageBox()
    msgbox.setText(" אילוצים שטופלו")
    #    msgbox.setInformativeText("טיפול באילוצים  " )
    msgbox.setDetailedText(str(info))
    msgbox.setWindowTitle("טיפול באילוצים")
    msgbox.exec()


def message_box():
    msgbox = QMessageBox()
    msgbox.setText(" גירסה 0.9")
    msgbox.setInformativeText(" תוכנה לסידור עבודה "
                              '\n'
                              "מחלקת אחזקה"
                              '\n'
                              "מלון רנסנס"
                              )

    #    msgbox.setDetailedText("The details are as follows:")
    msgbox.setWindowTitle("אחזקה")
    msgbox.exec()


def load_blank(self):
    self.constraints = []
    table = self.date_work_widget.weekWidget1
    for row in range(1, table.week_layout.rowCount()):
        row_data = []
        for column in range(1, table.week_layout.columnCount()):
            item = table.week_layout.itemAtPosition(row, column)
            if item is not None:
                try:
                    item.widget().setText('')
                    item.widget().getStyleSheet('')
                except AttributeError:
                    print('exception-load blank ', item.widget().text(), row, column)



def save_sheet(self):
    path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getcwd(), 'CSV(*.csv)')
    if path[0] != '':
        with open(path[0], 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            table = self.date_work_widget.weekWidget1
            for row in range(1, table.week_layout.rowCount()):
                row_data = []
                for column in range(1, table.week_layout.columnCount()):
                    item = table.week_layout.itemAtPosition(row, column)
                    if item is not None:
                        row_data.append(item.widget().text())
                    else:
                        print('else weekShift1 row  =', row, 'column=', column)
                print(row_data)
                writer.writerow(row_data)


def convert_add_constraint(self, txt, work_no, j, k):
    # Employee 1 wants a day off on tuesday.
    # Employee 4 wants a night shift on tuesday.
    # constraints = [(1, 0, 3, -2), (4, 2, 3, -2)]
    if k == 1:
        j += 6
    if txt == 'X':
        self.constraints.append((work_no, 0, j, -2))
    elif txt == '07-20' or txt == '07-15' or txt == '07-16':
        self.constraints.append((work_no, 1, j, -2))
    elif txt == '15-23':
        self.constraints.append((work_no, 2, j, -2))
    elif txt == '20-07' or txt == '23-07':
        self.constraints.append((work_no, 3, j, -2))
    elif txt == 'לא בוקר':
        self.constraints.append((work_no, 1, j, 4))
    elif txt == 'לא ערב':
        self.constraints.append((work_no, 3, j, 4))
        print('constraint; worker no %i , day no = %i  k = %i' % (work_no, j, k))
    elif txt == 'לא לילה':
        self.constraints.append((work_no, 3, j, 4))


def collect_constraints(self):
    table = self.date_work_widget.weekWidget1
    for row in range(1, table.week_layout.rowCount()):
        for column in range(1, table.week_layout.columnCount()):
            item = table.week_layout.itemAtPosition(row, column)
            if item != None:
                try:
                    info = item.widget().text()
                    convert_add_constraint(self, info, row - 2, column, 1)
                    #  remove date + workers start from 0
                except AttributeError:
                    print('item in convert ', item, 'row = ', row, 'col =', column)


def load_sheet_and_compute(self):
    """ Collect #########
    """
    # collect_constraints(self)
    load_sheet(self)
    # WeekShifts_Buttons.collect_weekend_constraints(self)
    # compute(self)
    # constriant_box(self.constraints)
    # self.constraints = []


def fill_table(table, i, row):
    for j in range(len(row)):
        text = row[j]
        old_widget = table.week_layout.itemAtPosition(i, j + 1)
        try:
            old_widget.widget().setText(text)
            old_widget.widget().getStyleSheet(text)
        except AttributeError:
            print('fill_table error', text, i, j)
            pass


def load_sheet(self):
    """ Load file to Application
    & Compute
    """
    shift_widget = self.date_work_widget.weekWidget1
    path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
    if path[0] != '':
        with open(path[0], newline='') as csv_file:
            my_file = csv.reader(csv_file, dialect='excel')
            for row in my_file:
                if my_file.line_num <= 7:
                    table_num = my_file.line_num
                    fill_table(shift_widget, table_num, row)
                # else:
                #     table = self.week_shifts_double.weekShift2
                #     table_num = my_file.line_num - 7
                #     fill_table(table, table_num, row)
        return True
    else:
        return False


def compute_date(self):

    dayName = MyDate(1).col_headers
    for i in range(len(dayName)):
        old_widget = self.date_work_widget.shiftWidget.week_layout.itemAtPosition(1, i + 1)
        try:
            old_widget.widget().setText(dayName[i])

        except AttributeError:
            print('first section', dayName[i])
#        k += 1


def convert_text(txt, j):
    if txt == 'O':
        return 'X'
    elif txt == 'M' and (j == 6 or j == 13):
        return '07-20'
    elif txt == 'M' and (j == 5 or j == 12):
        return '07-15'
    elif txt == 'M':
        return '07-16'
    elif txt == 'A':
        return '15-23'
    elif txt == 'N' and (j == 6 or j == 13):
        return '20-07'
    elif txt == 'N':
        return '23-07'


def compute(self):
    #
    self.compute_date()

    # Employee 1 wants a day off on tuesday.
    # Employee 4 wants a night shift on tuesday.
    # constraints = [(1, 0, 3, -2), (4, 2, 3, -2)]

    def split(word):
        return [char for char in word]

    solution = solve_shift_scheduling(self.constraints,1)

    for i in range(len(solution)):
        row = split(solution[i])
        for j in range(len(row)):
            #        for j in range(len(row)):
            orginal_text = row[j]
            text = convert_text(orginal_text, j)
            if j < 7:
                oldwidget = self.week_shifts_double.weekShift1.week_layout.itemAtPosition(i + 2, j + 1)
                try:
                    oldwidget.widget().setText(text)
                    oldwidget.widget().getStyleSheet(text)
                except AttributeError:
                    print('first section', text, i, j)

            # else:
            #     old_widget = self.week_shifts_double.weekShift2.week_layout.itemAtPosition(i + 2, j - 6)
            #     try:
            #         old_widget.widget().setText(text)
            #         old_widget.widget().getStyleSheet(text)
            #     except AttributeError:
            #         print('second section', text, i, j)


def handlePreview(self):
    dialog = QtPrintSupport.QPrintPreviewDialog()
    dialog.paintRequested.connect(self.handlePaintRequest)
    dialog.exec_()
