import Qt
from PyQt5 import QtWidgets
import sys

"""todo: faire une classe mere save asset, faire derriver SaveConceptGUI et Save_asset de cette classe """
class SaveConceptGUI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.init_ui()

    def init_ui(self):
        print("yaaa")
        self.setWindowTitle('Asset Manager')

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = SaveConceptGUI()
    app.exec_()

class SaveConceptGUI2:

    def __init__(self):
        self.asset_name = "test"
        self.asset_coords = {} #datas of the recorded asset
        self.main_layout = QtWidgets.QVBoxLayout()

    def gui(self):
        self.name_input = self.add_line_edit("name : ", self.asset_name)
        self.type_input = self.add_line_edit("Type : ", self.asset_name)
        self.task_input = self.add_line_edit("Task : ", self.asset_name)
        self.subtask_input = self.add_line_edit("Subtask : ", self.asset_name)
        self.version_input = self.add_line_edit("Version : ", "001")

        # buttons valid or cancel
        h_button_layout = QtWidgets.QHBoxLayout()
        button_validate = QtWidgets.QPushButton("Save")
        #button_validate.clicked.connect(self.save)
        h_button_layout.addWidget(button_validate)
        button_cancel = QtWidgets.QPushButton("Cancel")
        #button_cancel.clicked.connect(self.cancel)
        h_button_layout.addWidget(button_cancel)
        self.main_layout.addLayout(h_button_layout)
        return self.main_layout


    def add_line_edit(self, label, value):
        widget_name = QtWidgets.QLabel(label)
        self.main_layout.addWidget(widget_name)
        input_field = QtWidgets.QLineEdit(value)
        self.main_layout.addWidget(input_field)
        return input_field

    def show(self):
        # creation de l'application
        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        # creation de la fenetre
        self.mainWindow = QtWidgets.QMainWindow()

        main_layout = self.gui()
        self.mainWindow.setLayout(main_layout)

        self.mainWindow.show()
        # """
        # button = QtWidgets.QPushButton("Hello bande de batard !!")
        # button.show()
        # """
        self.app.exec_()

if __name__ == "__main__":
    main()
    
"""
#Code to test in the console : 

from pipeline.tools.engine.krita import gui_save_concept as gui
from PyQt5 import QtWidgets
import importlib
import sys

importlib.reload(gui)

app = QtWidgets.QApplication(sys.argv)
#ex = gui.SaveConceptGUI()
#sys.exit(app.exec_())"""
