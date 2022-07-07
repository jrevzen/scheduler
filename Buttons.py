import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QPushButton, QFrame, QVBoxLayout,
                             QTextEdit, QGridLayout, QLabel)


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

class Instructions(QFrame):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit(" הנחיות שימוש בתוכנה: "
                                  "\n\n"
                              "1. עדכן אילוצים בעזרת רבועי אילוצים למטה ."
                                  "\n\n"
                           " 2. טען קובץ תורנות ישן בעזרת לחיצה על כפתור 'טען קובץ ישן'.")
        self.textEdit.setReadOnly(True)
        # self.label_instruction = QLabel()
        # pixmap = QPixmap(resource_path("instructions.jpg"))
        # self.label_instruction.setPixmap(pixmap)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)
        self.setFrameShape(QFrame.Box)




class Buttons(QFrame):
    def __init__(self):
        super().__init__()

        self.button_compute = QPushButton('טען קובץ+צור סידור')
        self.button_load = QPushButton('טען קובץ')
        self.button_save = QPushButton('שמור קובץ')
        self.button_reset = QPushButton('אפס טבלאות')
        self.layout = QGridLayout()

        self.layout.addWidget(self.button_compute, 0, 2, 1, 2)
        self.layout.addWidget(self.button_load, 1, 1)
        self.layout.addWidget(self.button_save, 1, 2)
        self.layout.addWidget(self.button_reset, 1 ,3)

        self.setLayout(self.layout)
        self.setFrameShape(QFrame.Box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # file_demo = Instructions()
    file_demo = Buttons()
    file_demo.setWindowTitle('כפתורים')
    file_demo.update()
    file_demo.show()

    sys.exit(app.exec_())
