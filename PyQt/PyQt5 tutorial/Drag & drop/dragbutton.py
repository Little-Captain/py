from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    # reimplement two methods of the QPushButton:
    # the mouseMoveEvent() and the mousePressEvent()
    # The mouseMoveEvent() method is the place where
    # the drag and drop operation begins.
    def mouseMoveEvent(self, e):
        # Here we decide that we can perform
        # drag and drop only with a right mouse button.
        if e.buttons() != Qt.RightButton:
            return

        # The QDrag object is created.
        # The class provides support for MIME-based
        # drag and drop data transfer.
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        # The exec_() method of the drag object starts
        # the drag and drop operation.
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        # We specify the type of the drop action with setDropAction().
        # In our case it is a move action.
        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()