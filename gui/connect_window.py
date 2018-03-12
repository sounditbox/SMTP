#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtp
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout,\
    QLineEdit
from PyQt5.QtGui import QIcon

from gui import auth_window
from gui.I_window import I_window

class Connect_window (I_window):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 400, 200)
        self.setWindowTitle('Connection')
        self.setWindowIcon(QIcon('icon.jpg'))


        serverLabel = QLabel('SMTP server:')
        portLabel= QLabel('Port')
        self.serverEdit = QLineEdit('smtp.gmail.com')
        self.portEdit = QLineEdit('465')
        self.connBtn = QPushButton('Connect')

        grid = QGridLayout()
        grid.setSpacing(4)

        grid.addWidget(serverLabel, 2, 0)
        grid.addWidget(self.serverEdit, 2, 1)

        grid.addWidget(portLabel, 3, 0)
        grid.addWidget(self.portEdit, 3, 1)

        grid.addWidget(self.connBtn, 4, 0)

        # self.connBtn.clicked.connect(self.connect)

        self.setLayout(grid)
        self.center()
        self.show()

    # def connect(self):
    #     self.setDisabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Connect_window()

    sys.exit(app.exec_())