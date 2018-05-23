import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Drawing text')
        self.show()

    # Drawing is done within the paint event.
    def paintEvent(self, event):
        # The QPainter class is responsible for all the low-level painting.
        # All the painting methods go between begin() and end() methods.
        # The actual painting is delegated to the drawText() method.
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        # The drawText() method draws text on the window.
        # The rect() method of the paint event returns
        # the rectangle that needs to be updated.
        # With the Qt.AlignCenter we align the text in both dimensions.
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())