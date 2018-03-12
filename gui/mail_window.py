#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, \
    QLineEdit, QTextEdit, QRadioButton, QCheckBox
from PyQt5.QtGui import QIcon

from smtp import Smtp
from gui.I_window import I_window


class Mail_window(I_window):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle('Mail')
        self.setWindowIcon(QIcon('icon.jpg'))

        grid = QGridLayout()
        grid.setVerticalSpacing(8)
        grid.setHorizontalSpacing(4)

        from_label = QLabel('From:')
        self.from_edit = QLineEdit('python.smtp.test.mail@gmail.com')
        grid.addWidget(from_label, 0, 0)
        grid.addWidget(self.from_edit, 0, 1)

        to_label = QLabel('To:')
        self.to_edit = QLineEdit('python.smtp.test.mail1@gmail.com')
        grid.addWidget(to_label, 1, 0)
        grid.addWidget(self.to_edit, 1, 1)

        cc_label = QLabel('CC: ')
        self.cc_edit = QLineEdit('python.smtp.test.mail2@gmail.com')
        grid.addWidget(cc_label, 2, 0)
        grid.addWidget(self.cc_edit, 2, 1)

        bcc_label= QLabel('BCC:')
        self.bcc_edit = QLineEdit('python.smtp.test.mail3@gmail.com')
        grid.addWidget(bcc_label, 3, 0)
        grid.addWidget(self.bcc_edit, 3, 1)

        subj_label = QLabel('Subject:')
        self.subj_edit = QLineEdit('example_subject')
        grid.addWidget(subj_label, 4, 0)
        grid.addWidget(self.subj_edit, 4, 1)

        self.text_type = QCheckBox('as html')
        grid.addWidget(self.text_type, 5, 0)

        msg_label = QLabel('Message:')
        self.msg_edit = QTextEdit('example message')
        grid.addWidget(msg_label, 6, 0)
        grid.addWidget(self.msg_edit, 6, 1)

        self.sendBtn = QPushButton('Send')
        self.attachBtn = QPushButton('Attach')
        grid.addWidget(self.attachBtn, 7,0)
        grid.addWidget(self.sendBtn, 7, 1)

        # self.sendBtn.clicked.connect(self.send)
        # self.attachBtn.clicked.connect(self.attach)

        self.setLayout(grid)
        self.center()
        self.show()

    # def send(self):
    #     pass

    # def attach(self):
    #     print('attach')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mail_window()
    sys.exit(app.exec_())