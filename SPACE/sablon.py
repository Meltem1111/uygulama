import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow
from tablep import Ui_MainWindow
import sys

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


def app():
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
app()