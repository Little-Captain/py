from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
import sys

# In order to drop text on the QPushButton widget,
# we must reimplement some methods.
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        # enable drop events for the widget with setAcceptDrops().
        self.setAcceptDrops(True)

    # reimplement the dragEnterEvent() method.
    # We inform about the data type that we accept.
    # In our case it is plain text.
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # reimplementing the dropEvent() method
    # we define what happes at the drop event.
    # Here we change the text of the button widget.
    def dropEvent(self, e):

        self.setText(e.mimeData().text())
        self.adjustSize()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        # The QLineEdit widget has a built-in support for drag operations.
        # All we need to do is to call the setDragEnabled() method to activate it.
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()