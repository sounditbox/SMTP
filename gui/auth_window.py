#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, \
    QGridLayout, QLineEdit, QRadioButton, QCheckBox
from PyQt5.QtGui import QIcon

from gui.I_window import I_window

class Auth_window (I_window):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 350, 150)
        self.setWindowTitle('Authorisation  ')
        self.setWindowIcon(QIcon('icon.jpg'))

        loginLabel = QLabel('Login:')
        passwdLabel = QLabel('Password:')

        self.loginEdit = QLineEdit('python.smtp.test.mail@gmail.com')
        self.passwdEdit = QLineEdit('pythonpython')
        self.passwdEdit.setEchoMode(QLineEdit.Password)

        self.loginBtn = QPushButton('Log in')

        grid = QGridLayout()
        grid.setSpacing(4)

        grid.addWidget(loginLabel, 1, 0)
        grid.addWidget(self.loginEdit, 1, 1)

        grid.addWidget(passwdLabel, 2, 0)
        grid.addWidget(self.passwdEdit, 2, 1)

        grid.addWidget(self.loginBtn, 4, 0)

        # self.loginBtn.clicked.connect(self.login)

        self.setLayout(grid)
        self.center()
        self.show()

    # def login(self):
    #     print('logging in')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Auth_window()
    sys.exit(app.exec_())