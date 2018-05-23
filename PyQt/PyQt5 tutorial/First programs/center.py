import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 自己的 Geometry
        qr = self.frameGeometry()
        # The QDesktopWidget class provides information
        # about the user's desktop, including the screen size.
        # 获取设备 Geometry, 并返回 center point
        cp = QDesktopWidget().availableGeometry().center()
        # 将 qr 的中心移到设备中心(cp)
        qr.moveCenter(cp)
        # 将 自己 移动到 qr 的左上点, 这样整个窗口就在屏幕中心了
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())