"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        # The super() method returns the parent object of the Example class
        # and we call its constructor.
        super().__init__()
        # The creation of the GUI is delegated to the initUI() method.
        self.initUI()

    def initUI(self):
        # In fact, it combines the resize()
        # and move() methods in one method.
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        # sets the application icon
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())