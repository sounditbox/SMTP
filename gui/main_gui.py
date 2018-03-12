#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtp
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, \
    QLineEdit, QTextEdit, QCheckBox, QStackedLayout, QStackedWidget, QWidget, QDialog, QFileDialog
from PyQt5.QtGui import QIcon

from gui.I_window import I_window
from gui.auth_window import Auth_window
from gui.mail_window import Mail_window
from gui.connect_window import Connect_window
from smtp import Smtp

class Main_window(I_window):

    def __init__(self):

        super().__init__()
        self.setGeometry(0, 0, 1000, 900)
        self.setWindowTitle('SMTP')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.init_ui()

        self.attachments = []

    def init_ui(self):

        grid = QGridLayout()
        grid.setVerticalSpacing(2)
        grid.setHorizontalSpacing(2)

        self.auth = Auth_window()
        self.mail = Mail_window()
        self.conn = Connect_window()
        self.auth.setDisabled(True)
        self.mail.setDisabled(True)
        grid.addWidget(self.conn,0,0)
        grid.addWidget(self.auth,0,1)
        grid.addWidget(self.mail,1,0,2,2)

        self.conn.connBtn.clicked.connect(self.connect)
        self.auth.loginBtn.clicked.connect(self.login)
        self.mail.sendBtn.clicked.connect(self.send)
        self.mail.attachBtn.clicked.connect(self.attach)


        self.setLayout(grid)
        self.center()
        self.show()

    def connect(self):
        self.conn.setDisabled(True)
        self.auth.setEnabled(True)

    def login(self):
        self.auth.setDisabled(True)
        self.mail.setEnabled(True)


    def send(self):
        ip = self.conn.serverEdit.text()
        port = self.conn.portEdit.text()
        username = self.auth.loginEdit.text()
        password = self.auth.passwdEdit.text()
        boundary = '--boundary42'
        mail_from = self.mail.from_edit.text()
        mail_to = self.mail.to_edit.text()
        cc = self.mail.cc_edit.text()
        bcc = self.mail.bcc_edit.text()
        subj = self.mail.subj_edit.text()
        mes = self.mail.msg_edit.toPlainText()
        text_type = 'html' if self.mail.text_type.isTristate() else 'plain'
        attachments = self.attachments if len(self.attachments) > 0 else None
        smtp = Smtp(ip,port,
                    username,password,
                    boundary,mail_from,mail_to,cc,bcc,subj,mes,
                    text_type, attachments)
        smtp.send_mail()

    def attach(self):
        self.attachments.append(QFileDialog.getOpenFileName(self)[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_window()
    sys.exit(app.exec_())