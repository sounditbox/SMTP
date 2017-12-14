#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtp
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout,\
    QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon

from gui.I_window import I_window


class Mail_window(I_window):

    def __init__(self,smtp):
        self.smtp = smtp

        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('Mail')
        self.setWindowIcon(QIcon('icon.jpg'))

        toLabel = QLabel('Send mail to:')
        ccLabel = QLabel('Send copy to: ')
        bccLabel= QLabel('Black copy to:')
        subjLabel = QLabel('Subject:')
        msgLabel = QLabel('Message:')

        toEdit = QLineEdit()
        ccEdit = QLineEdit()
        bccEdit = QLineEdit()
        subjEdit = QLineEdit()
        msgEdit = QTextEdit()

        sendBtn = QPushButton('Send')
        attachBtn = QPushButton('Attach')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(toLabel, 1, 0)
        grid.addWidget(toEdit, 1, 1)

        grid.addWidget(ccLabel, 2, 0)
        grid.addWidget(ccEdit, 2, 1)

        grid.addWidget(bccLabel, 3, 0)
        grid.addWidget(bccEdit, 3, 1)

        grid.addWidget(subjLabel, 4, 0)
        grid.addWidget(subjEdit, 4, 1)


        grid.addWidget(msgLabel, 5, 0)
        grid.addWidget(msgEdit, 5, 1, 4, 1)

        grid.addWidget(attachBtn, 10,0)
        grid.addWidget(sendBtn, 10, 1)

        sendBtn.clicked.connect(self.send)
        attachBtn.clicked.connect(self.attach)

        self.setLayout(grid)
        self.center()
        self.show()

    def send(self):
        print('send')

    def attach(self):
        print('attach')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mail_window()
    sys.exit(app.exec_())