import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # Mouse tracking is disabled by default,
        # so the widget only receives mouse move events
        # when at least one mouse button is pressed
        # while the mouse is being moved.
        # If mouse tracking is enabled, the widget receives
        # mouse move events even if no buttons are pressed.
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    # The e is the event object; it contains data
    # about the event that was triggered; in our case,
    # a mouse move event. With the x() and y() methods
    # we determine the x and y coordinates of the mouse pointer.
    # We build the string and set it to the label widget.
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())