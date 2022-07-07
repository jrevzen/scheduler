import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QFrame
from PyQt5.QtGui import QDrag, QPixmap, QPainter
from PyQt5.QtCore import QMimeData, Qt


class DraggableLabel(QLabel):

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setFrameShape(QFrame.Box)
        txt = self.text()
        self.getStyleSheet(txt)
        self.setFixedSize(70, 25)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setColorData(self.colorCount())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def getStyleSheet(self, txt):
        if txt == 'לא בוקר' or txt == '07-16' or txt == '07-14.5' or txt == '07-15' or txt == '07-20':
            return self.setStyleSheet("background:yellow")
        elif txt == '15-23' or txt == '14.5-23' or txt == 'לא ערב':
            return self.setStyleSheet("background:coral")
        elif txt == '23-07' or txt == 'לא לילה' or txt == '20-07':
            return self.setStyleSheet("background:aqua")
        elif txt == 'X':
            return self.setStyleSheet("background:white")
        else:
            return self.setStyleSheet("background:white")


class DropLabel(QLabel):

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.setFrameShape(QFrame.Box)
        txt = self.text()
        self.getStyleSheet(txt)
        self.setFixedSize(70, 25)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.pos()
        text = event.mimeData().text()
        self.getStyleSheet(text)
        self.setText(text)
        event.acceptProposedAction()

    def getStyleSheet(self, txt):
        if txt == 'לא בוקר' or txt == '07-16' or txt == '07-14.5' or txt == '07-15' or txt == '07-20':
            return self.setStyleSheet("background:yellow")
        elif txt == '15-23' or txt == '14.5-23' or txt == 'לא ערב':
            return self.setStyleSheet("background:coral")
        elif txt == '23-07' or txt == 'לא לילה' or txt == '20-07':
            return self.setStyleSheet("background:aqua")
        elif txt == 'X':
            return self.setStyleSheet("background:white")
        else:
            return self.setStyleSheet("background:white")


class Drag_Label_deny(QFrame):
    def __init__(self):
        super().__init__()

        label_not07 = DraggableLabel("לא בוקר", self)
        label_not15 = DraggableLabel("לא ערב", self)
        label_not23 = DraggableLabel("לא לילה", self)
        label_head = QLabel('בקשות אחרות')

        layout = QGridLayout()
        layout.addWidget(label_head, 0, 0, 1, 3)
        layout.addWidget(label_not07, 1, 0)
        layout.addWidget(label_not15, 1, 1)
        layout.addWidget(label_not23, 1, 2)
        self.setLayout(layout)
        self.setFrameShape(QtWidgets.QFrame.Box)


class Drag_Label(QFrame):
    def __init__(self):
        super().__init__()

        label07 = DraggableLabel("07-16", self)
        label15 = DraggableLabel("15-23", self)
        label23 = DraggableLabel("23-07", self)
        labelx = DraggableLabel("X", self)
        label_none = DraggableLabel('',self)
        label_head = QLabel('אילוצים')

        layout = QGridLayout()
        layout.addWidget(label_head, 0, 0, 1, 3)
        layout.addWidget(label07, 1, 0)
        layout.addWidget(label15, 1, 1)
        layout.addWidget(label23, 1, 2)
        layout.addWidget(labelx, 2, 1)
        layout.addWidget(label_none,2,0)
        self.setLayout(layout)
        self.setFrameShape(QtWidgets.QFrame.Box)


class Drag_Label_Holiday(QFrame):
    def __init__(self):
        super().__init__()
        label_head = QLabel('אילוצי שבת/חג')
        label07 = DraggableLabel("07-15", self)
        label0720 = DraggableLabel("07-20", self)
        label20 = DraggableLabel("20-07", self)

        layout = QGridLayout()
        layout.addWidget(label_head, 0, 0, 1, 3)
        layout.addWidget(label07, 1, 0)
        layout.addWidget(label0720, 1, 1)
        layout.addWidget(label20, 1, 2)
        self.setLayout(layout)
        self.setFrameShape(QtWidgets.QFrame.Box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Drag_Label_deny()
    w.show()

    sys.exit(app.exec_())
