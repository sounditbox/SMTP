import sys
from PyQt5.QtWidgets import QApplication

from gui.main_gui import Main_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_window()
    sys.exit(app.exec_())