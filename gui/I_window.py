#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smtp
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QHBoxLayout, QGridLayout, \
    QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon


class I_window(QWidget):

    def __init__(self):
        super().__init__()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = I_window()
    sys.exit(app.exec_())