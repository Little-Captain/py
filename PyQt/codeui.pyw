#import sys
#from PyQt5 import QtWidgets, QtCore
#class demowind(QtWidgets.QWidget):
#    def __init__(self, parent = None):
#        QtWidgets.QWidget.__init__(self, parent)
#        self.setGeometry(300, 300, 200, 200)
#        self.setWindowTitle('Demo window')
#        quit = QtWidgets.QPushButton('Close', self)
#        quit.setGeometry(10, 10, 70, 40)
#        quit.clicked.connect(QtCore.quit())
#app = QtWidgets.QApplication(sys.argv)
#dw = demowind()
#dw.show()
#sys.exit(app.exec_())
from PyQt5.QtWidgets import *
import sys

class LoginDlg(QDialog):
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)
        usr = QLabel("用户：")
        pwd = QLabel("密码：")
        self.usrLineEdit = QLineEdit()
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3);
        gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 3);

        okBtn = QPushButton("确定")
        cancelBtn = QPushButton("取消")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        self.setWindowTitle("登录")
        self.resize(300, 200)

    def accept(self):
        if self.usrLineEdit.text().strip() == "eric" and self.pwdLineEdit.text() == "eric":
            super(LoginDlg, self).accept()
        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.usrLineEdit.setFocus()

app = QApplication(sys.argv)
dlg = LoginDlg()
dlg.show()
dlg.exec_()
app.exit()
