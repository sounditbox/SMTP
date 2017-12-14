#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtp
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout,\
    QLineEdit
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

        hostLabel = QLabel('Hostname:')
        serverLabel = QLabel('SMTP server:')
        portLabel= QLabel('Port')

        hostEdit = QLineEdit()
        serverEdit = QLineEdit()
        portEdit = QLineEdit()

        connBtn = QPushButton('Connect')

        grid = QGridLayout()
        grid.setSpacing(4)

        grid.addWidget(hostLabel, 1, 0)
        grid.addWidget(hostEdit, 1, 1)

        grid.addWidget(serverLabel, 2, 0)
        grid.addWidget(serverEdit, 2, 1)

        grid.addWidget(portLabel, 3, 0)
        grid.addWidget(portEdit, 3, 1)

        grid.addWidget(connBtn, 4, 0)


        connBtn.clicked.connect(self.connect)

        self.setLayout(grid)
        self.center()
        self.show()

    def connect(self):
        print('connect')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Connect_window()
    sys.exit(app.exec_())