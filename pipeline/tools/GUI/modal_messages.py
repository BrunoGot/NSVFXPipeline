import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui,QtCore
from PyQt6.QtWidgets import QDialog

class ErrorDialog(QDialog):
    def __init__(self,msg, details = ''):
        super().__init__()
        self.setWindowTitle("Error !")
        ok_btn = QtWidgets.QPushButton("OK")
        ok_btn.clicked.connect(self.ok_click)
        self.layout = QtWidgets.QVBoxLayout()
        error_label = QtWidgets.QLabel("error : ")
        label_msg = QtWidgets.QLabel(msg)
        label_detail = QtWidgets.QLabel(details)
        self.layout.addWidget(error_label)
        self.layout.addWidget(label_msg)
        self.layout.addWidget(label_detail)
        self.layout.addWidget(ok_btn)
        self.setLayout(self.layout)


    def ok_click(self):
        self.close()

def error(msg, raw_error=''):
    app = QtWidgets.QApplication(sys.argv)
    dlg = ErrorDialog(msg, raw_error)
    print("error")
    dlg.setWindowTitle(msg)
    dlg.show()
    app.exec_()