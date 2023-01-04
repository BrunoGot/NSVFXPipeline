import sys
import os

#from krita import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets as qt

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs

"""todo: faire une classe mere save asset, faire derriver SaveConceptGUI et Save_asset de cette classe """
class SaveConceptGUI(qt.QWidget):
    def __init__(self, parent=None):
        qt.QWidget.__init__(self)
        self.setParent(parent, QtCore.Qt.Window)
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Asset Manager')
        self.setGeometry(10,10,640,480)
        self.mainlayout = qt.QVBoxLayout()
        ##lines
        self.project_line = self.add_line_edit("Project : ", "")
        self.asset_line = self.add_line_edit("Asset : ", "")
        self.task_line = self.add_line_edit("Task : ", "")
        self.subtask_line = self.add_line_edit("Subtask : ", "")
        self.iteration_line = self.add_line_edit("Iteration : ", "")
        self.action_layout = qt.QHBoxLayout()
        self.save_button = qt.QPushButton("Save Asset")
        #self.save_button.clicked.connect(self.save)
        self.action_layout.addWidget(self.save_button)
        self.connect(self.save_button, QtCore.SIGNAL('clicked()'),self.save)
        self.cancel_button = qt.QPushButton("Cancel Asset")
        self.cancel_button.clicked.connect(self.cancel)
        self.action_layout.addWidget(self.cancel_button)
        self.mainlayout.addLayout(self.action_layout)
        self.console = qt.QLabel("")
        self.mainlayout.addWidget(self.console)
        self.mainlayout.addWidget(self.save_button)
        self.setLayout(self.mainlayout)
        self.show()

    def add_line_edit(self, label, value):
        layout = qt.QHBoxLayout()
        widget_name = qt.QLabel(label)
        layout.addWidget(widget_name)
        input_field = qt.QLineEdit(value)
        layout.addWidget(input_field)
        self.mainlayout.addLayout(layout)
        return input_field

    def save(self):
        #check input value
        try:
            project = self.project_line.text()
            asset = self.asset_line.text()
            task = self.task_line.text()
            subtask = self.subtask_line.text()
            iteration = self.iteration_line.text()
            #if they are good :
            error_msg, check_value_flag = self.check_value(project, asset, task, subtask, iteration)
            if check_value_flag is True:
                # configure path
                asset_datas = {"AssetType" : project, "AssetName" : asset, "Task" : task, "Subtask" : subtask, "Version": iteration, "ext" : "kra"}
                base_path = engine.make_asset_path(asset_datas) #same in blender_shelf save_asset
                path_id = os.path.join(base_path, fs.conf.asset_file_name.format(asset_datas))
                print("path ready to save = {}".format(path_id))
                self.event_flag = True

                """
                to move in krita engine
                """
                """doc = Krita.instance().activeDocument()
                if os.path.exists(doc.fileName()):  # si le fichier a déja été sauvegardé une fois
                    doc.setFileName(path_id)
                    doc.save()
                else:
                    doc.saveAs(path_id)"""

                self.close()
            else: #print an error message
                self.console.setText(error_msg)
        except Exception as e:
            self.console.setText("Error while saving : {0}".format(e))

    def cancel(self):
        self.close()

    def get_path_id(self, name, type, task, subtask, version):
        asset_datas = {"AssetType": type, "AssetName": name, "Task": task, "Subtask": subtask, "Version": version, "ext":self.asset_ext}
        path_id = engine.make_asset_path(asset_datas)
        #asset_file_path = fs.conf.asset_file_name.format(asset_datas)
        path_id = os.path.join(path_id,fs.conf.asset_file_name.format(asset_datas))
        return path_id

    def check_value(self, name, type, task, subtask, version):
        flag = True
        error = ""
        error_msg = "can't be empty"
        if name == "":
            error = "name "+error_msg
            flag = False
        elif type == "":
            error = "type "+error_msg
            flag = False
        elif task == "":
            error = "task "+error_msg
            flag = False
        elif subtask == "":
            error = "subtask"+error_msg
            flag = False
        elif version == "":
            error = "version"+error_msg
            flag = False
        return error, flag

def main():
    print("main")
    app = qt.QApplication(sys.argv)
    ex = SaveConceptGUI()
    app.exec_()

class SaveConceptGUI2:

    def __init__(self):
        self.asset_name = "test"
        self.asset_coords = {} #datas of the recorded asset
        self.main_layout = qt.QVBoxLayout()

    def gui(self):
        self.name_input = self.add_line_edit("name : ", self.asset_name)
        self.type_input = self.add_line_edit("Type : ", self.asset_name)
        self.task_input = self.add_line_edit("Task : ", self.asset_name)
        self.subtask_input = self.add_line_edit("Subtask : ", self.asset_name)
        self.version_input = self.add_line_edit("Version : ", "001")

        # buttons valid or cancel
        h_button_layout = qt.QHBoxLayout()
        button_validate = qt.QPushButton("Save")
        #button_validate.clicked.connect(self.save)
        h_button_layout.addWidget(button_validate)
        button_cancel = qt.QPushButton("Cancel")
        #button_cancel.clicked.connect(self.cancel)
        h_button_layout.addWidget(button_cancel)
        self.main_layout.addLayout(h_button_layout)
        return self.main_layout


    def add_line_edit(self, label, value):
        widget_name = qt.QLabel(label)
        self.main_layout.addWidget(widget_name)
        input_field = qt.QLineEdit(value)
        self.main_layout.addWidget(input_field)
        return input_field

    def show(self):
        # creation de l'application
        if not qt.QApplication.instance():
            self.app = qt.QApplication(sys.argv)
        else:
            self.app = qt.QApplication.instance()

        # creation de la fenetre
        self.mainWindow = qt.QMainWindow()

        main_layout = self.gui()
        self.mainWindow.setLayout(main_layout)

        self.mainWindow.show()
        # """
        # button = qt.QPushButton("Hello bande de batard !!")
        # button.show()
        # """
        #self.show()


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
