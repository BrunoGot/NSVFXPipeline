import sys
import os

from krita import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets as qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs

from PyQt5.QtWidgets import QLineEdit, QGraphicsRectItem, QGraphicsView, QVBoxLayout, QMainWindow, QGraphicsScene, QLabel, QPushButton, QHBoxLayout, QSpinBox, QSlider, QCheckBox, QScrollArea, QWidget, QApplication, QColorDialog, QGraphicsItem
from PyQt5.Qt import Qt
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from PyQt5.QtGui import QColor, QImage


"""todo: faire une classe mere save asset, faire derriver SaveConceptGUI et Save_asset de cette classe """
class SaveConceptGUI(DockWidget):
    project_structure = {}
    def add_pipeline_folder(self, label_name):
        layout = QHBoxLayout()
        project_label = QLabel(label_name)
        layout.addWidget(project_label)
        project_line_edit = QLineEdit()
        layout.addWidget(project_line_edit)
        self.project_structure[label_name] = project_line_edit
        return layout

    def __init__(self, parent):
        """
        inspired from https://github.com/rogudator/rogudators_comic_panel_generator
        :param parent: qwindows or widget to attach to
        """
        super().__init__()
        QWidget.__init__(self)

        #self.setParent(parent)
        #self.setParent(parent, QtCore.Qt.Window) #to get a windows framed ui

        self.setWindowTitle("Rogudator's comic panel generator")

        mainLayout = QVBoxLayout()
        l_preview = QLabel(self)
        l_preview.setText("Preview:")
        mainLayout.addWidget(l_preview)


        mainLayout.addLayout(self.add_pipeline_folder("Project"))
        mainLayout.addLayout(self.add_pipeline_folder("Name"))
        mainLayout.addLayout(self.add_pipeline_folder("Task"))
        mainLayout.addLayout(self.add_pipeline_folder("Subtask"))
        mainLayout.addLayout(self.add_pipeline_folder("Version"))

        button_layout = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        button_layout.addWidget(cancel_btn)

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save)
        button_layout.addWidget(self.save_btn)

        self.console = QLabel("console")
        mainLayout.addWidget(self.console)

        mainLayout.addLayout(button_layout)


        self.scrollMainLayout = QScrollArea(self)
        self.scrollMainLayout.setWidgetResizable(True)
        self.scrollMainLayout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.window = QWidget(self)
        self.window.setLayout(mainLayout)
        self.scrollMainLayout.setWidget(self.window)
        self.setWidget(self.scrollMainLayout)
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
            project = self.project_structure["Project"].text()
            asset = self.project_structure["Name"].text()
            task = self.project_structure["Task"].text()
            subtask = self.project_structure["Subtask"].text()
            iteration = self.project_structure["Version"].text()
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
                doc = Krita.instance().activeDocument()
                if os.path.exists(doc.fileName()):  # si le fichier a déja été sauvegardé une fois
                    doc.setFileName(path_id)
                    doc.save()
                else:
                    doc.saveAs(path_id)

                self.close()
            else: #print an error message
                self.console.setText(error_msg)
        except Exception as e:
            self.console.setText("Error while saving : {0}".format(e))

    def cancel(self):
        self.close()

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
