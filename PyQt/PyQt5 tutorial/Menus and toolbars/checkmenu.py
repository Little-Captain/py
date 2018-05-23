import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        # 针对 macOS 适配
        menubar.setNativeMenuBar(False)
        viewMenu = menubar.addMenu('View')
        # 创建 action, 使能 check
        viewStatAct = QAction('View statusbar', self, checkable=True)
        # 设置相应的状态栏提示
        viewStatAct.setStatusTip('View statusbar')
        # 默认 checked
        viewStatAct.setChecked(True)
        # 连接方法 toggleMenu
        viewStatAct.triggered.connect(self.toggleMenu)
        # 添加 action
        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):
        # 根据状态设置状态栏是否隐藏
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())