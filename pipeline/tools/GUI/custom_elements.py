import sys
import PyQt6
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import pyqtSignal as Signal


class NsQlineEdit(QtWidgets.QLineEdit):

    clicked = Signal()

    def mousePressEvent(self, event):
        super(NsQlineEdit, self).mousePressEvent(event)
        self.clicked.emit()
"""
####test####
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lineedit = NsQlineEdit()
        self.lineedit.clicked.connect(self.lineedit.clear)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.lineedit)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
    
    #####
"""