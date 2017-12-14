#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtp
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton,\
    QGridLayout, QLineEdit,  QRadioButton
from PyQt5.QtGui import QIcon

from gui.I_window import I_window


class Connect_window (I_window):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 500, 200)
        self.setWindowTitle('Connect')
        self.setWindowIcon(QIcon('icon.jpg'))

        loginLabel = QLabel('Login:')
        passwdLabel = QLabel('Password:')
        tlsLabel = QLabel('Use TLS')

        loginEdit = QLineEdit()
        passwdEdit = QLineEdit()
        passwdEdit.setEchoMode(QLineEdit.Password)

        tlsRadButt = QRadioButton()

        loginBtn = QPushButton('Log in')

        grid = QGridLayout()
        grid.setSpacing(4)

        grid.addWidget(loginLabel, 1, 0)
        grid.addWidget(loginEdit, 1, 1)

        grid.addWidget(passwdLabel, 2, 0)
        grid.addWidget(passwdEdit, 2, 1)

        grid.addWidget(tlsLabel, 3, 0)
        grid.addWidget(tlsRadButt, 3, 1)

        grid.addWidget(loginBtn, 4, 0)

        loginBtn.clicked.connect(self.login)

        self.setLayout(grid)
        self.center()
        self.show()

    def login(self):
        print('logging in')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Connect_window()
    sys.exit(app.exec_())