import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]
        # zip : zip([1, 2], [3, 4]) => [(1, 3), (2, 4)] (zip object)
        # 同时遍历 position、name
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            # Python 允许你在 list 或 tuple 前面加一个 * 号，
            # 把 list 或 tuple 的元素变成可变参数传进去
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())