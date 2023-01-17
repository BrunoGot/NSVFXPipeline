import sys
import os

from krita import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets as qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs

from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsView, QVBoxLayout, QMainWindow, QGraphicsScene, QLabel, QPushButton, QHBoxLayout, QSpinBox, QSlider, QCheckBox, QScrollArea, QWidget, QApplication, QColorDialog, QGraphicsItem
from PyQt5.Qt import Qt
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from PyQt5.QtGui import QColor, QImage


"""todo: faire une classe mere save asset, faire derriver SaveConceptGUI et Save_asset de cette classe """
class SaveConceptGUI(DockWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rogudator's comic panel generator")

        mainLayout = QVBoxLayout()

        # l means label
        # b means push button
        # sp means spinbox
        # sl means slider
        # cb means combobox

        l_preview = QLabel(self)
        l_preview.setText("Preview:")
        mainLayout.addWidget(l_preview)

        #self.rcpg_object = RCPG()
        #self.rcpg_object.refresh_svg_renderer()

        #renderer = self.rcpg_object.svg_renderer
        self.svg_item = QGraphicsSvgItem()
        #self.svg_item.setSharedRenderer(renderer)

        #self.preview = Page_preview()
        #self.preview.scene().addItem(self.svg_item)
        #mainLayout.addWidget(self.preview)

        #self.set_clickable_gutters()

        l_generate = QLabel(self)
        l_generate.setText("Generate as:")
        mainLayout.addWidget(l_generate)

        b_layer = QPushButton(self)
        b_layer.setText("Layer")

        b_file = QPushButton(self)
        b_file.setText("File")

        file_and_layer = QHBoxLayout(self)
        file_and_layer.addWidget(b_layer)
        file_and_layer.addWidget(b_file)
        mainLayout.addLayout(file_and_layer)

        l_num_rows = QLabel(self)
        l_num_rows.setText("Number of rows:")
        mainLayout.addWidget(l_num_rows)

        self.sp_num_rows = QSpinBox(self)
        self.sp_num_rows.setValue(2)
        self.sp_num_rows.setMinimum(1)

        self.sl_num_rows = QSlider(self)
        self.sl_num_rows.setMinimum(1)
        self.sl_num_rows.setMaximum(6)
        self.sl_num_rows.setOrientation(Qt.Horizontal)
        self.sl_num_rows.setTickPosition(1)
        self.sl_num_rows.setTickInterval(1)
        self.sl_num_rows.setMinimumWidth(100)
        self.sl_num_rows.setValue(2)

        num_rows = QHBoxLayout(self)
        num_rows.addWidget(self.sp_num_rows)
        num_rows.addWidget(self.sl_num_rows)
        mainLayout.addLayout(num_rows)

        l_num_columns = QLabel(self)
        l_num_columns.setText("Numer of columns:")
        mainLayout.addWidget(l_num_columns)

        self.sp_num_columns = QSpinBox(self)
        self.sp_num_columns.setValue(2)
        self.sp_num_columns.setMinimum(1)

        self.sl_num_columns = QSlider(self)
        self.sl_num_columns.setMinimum(1)
        self.sl_num_columns.setMaximum(6)
        self.sl_num_columns.setOrientation(Qt.Horizontal)
        self.sl_num_columns.setTickPosition(1)
        self.sl_num_columns.setTickInterval(1)
        self.sl_num_columns.setMinimumWidth(100)
        self.sl_num_columns.setValue(2)

        num_columns = QHBoxLayout(self)
        num_columns.addWidget(self.sp_num_columns)
        num_columns.addWidget(self.sl_num_columns)
        mainLayout.addLayout(num_columns)

        l_gutter = QLabel(self)
        l_gutter.setText("Gutters")
        mainLayout.addWidget(l_gutter)

        self.cb_gutter_equal = QCheckBox(self)
        self.cb_gutter_equal.setText("Horizontal and vertical gutters are equal")
        self.cb_gutter_equal.setChecked(True)
        mainLayout.addWidget(self.cb_gutter_equal)

        l_hgutter = QLabel(self)
        l_hgutter.setText("Size of a horizontal gutter:")
        mainLayout.addWidget(l_hgutter)

        self.hgutter_updated = True

        #self.hgutter_max = int(self.rcpg_object.height_page / (self.rcpg_object.rows + 1))

        self.sp_hgutter = QSpinBox(self)
        self.sp_hgutter.setValue(30)
        self.sp_hgutter.setMinimum(1)
        #self.sp_hgutter.setMaximum(self.hgutter_max)

        self.sl_hgutter = QSlider(self)
        self.sl_hgutter.setMaximum(1)
        #self.sl_hgutter.setMaximum(self.hgutter_max)
        self.sl_hgutter.setOrientation(Qt.Horizontal)
        self.sl_hgutter.setTickInterval(1)
        self.sl_hgutter.setMinimumWidth(100)
        self.sl_hgutter.setValue(30)

        hgutter = QHBoxLayout(self)
        hgutter.addWidget(self.sp_hgutter)
        hgutter.addWidget(self.sl_hgutter)
        mainLayout.addLayout(hgutter)

        l_vgutter = QLabel(self)
        l_vgutter.setText("Size of a vertical gutter:")
        mainLayout.addWidget(l_vgutter)

        self.vgutter_updated = True

        #self.vgutter_max = int(self.rcpg_object.width_page / (self.rcpg_object.columns + 1))

        self.sp_vgutter = QSpinBox(self)
        self.sp_vgutter.setValue(30)
        self.sp_vgutter.setMinimum(1)
        #self.sp_vgutter.setMaximum(self.vgutter_max)

        self.sl_vgutter = QSlider(self)
        self.sl_vgutter.setMaximum(1)
        #self.sl_vgutter.setMaximum(self.vgutter_max)
        self.sl_vgutter.setOrientation(Qt.Horizontal)
        self.sl_vgutter.setTickInterval(1)
        self.sl_vgutter.setMinimumWidth(100)
        self.sl_vgutter.setValue(30)

        vgutter = QHBoxLayout(self)
        vgutter.addWidget(self.sp_vgutter)
        vgutter.addWidget(self.sl_vgutter)
        mainLayout.addLayout(vgutter)

        l_cgutter = QLabel(self)
        l_cgutter.setText("Color of the gutter:")
        mainLayout.addWidget(l_cgutter)

        self.l_color_gutter = QLabel(self)
        self.l_color_gutter.setText("#000000")

        b_color_gutter = QPushButton(self)
        b_color_gutter.setText("Change")

        color_of_gutter = QHBoxLayout(self)
        color_of_gutter.addWidget(self.l_color_gutter)
        color_of_gutter.addWidget(b_color_gutter)
        mainLayout.addLayout(color_of_gutter)

        l_outline = QLabel(self)
        l_outline.setText("Size of panel outline:")
        mainLayout.addWidget(l_outline)

        self.sp_outline = QSpinBox(self)
        self.sp_outline.setValue(6)
        self.sp_outline.setMinimum(0)

        self.sl_outline = QSlider(self)
        self.sl_outline.setMinimum(0)
        self.sl_outline.setMaximum(98)
        self.sl_outline.setOrientation(Qt.Horizontal)
        self.sl_outline.setTickInterval(1)
        self.sl_outline.setMinimumWidth(100)
        self.sl_outline.setValue(6)

        outline = QHBoxLayout(self)
        outline.addWidget(self.sp_outline)
        outline.addWidget(self.sl_outline)
        mainLayout.addLayout(outline)

        l_color_outline = QLabel(self)
        l_color_outline.setText("Color of panel outline:")
        mainLayout.addWidget(l_color_outline)

        self.l_color_outline = QLabel(self)
        self.l_color_outline.setText("#ffffff")

        b_color_outline = QPushButton(self)
        b_color_outline.setText("Change")

        color_of_outline = QHBoxLayout(self)
        color_of_outline.addWidget(self.l_color_outline)
        color_of_outline.addWidget(b_color_outline)
        mainLayout.addLayout(color_of_outline)

        self.scrollMainLayout = QScrollArea(self)
        self.scrollMainLayout.setWidgetResizable(True)
        self.scrollMainLayout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        """b_file.clicked.connect(self.b_file_create)
        b_layer.clicked.connect(self.b_layer_create)
        self.sp_num_rows.valueChanged.connect(self.upd_sp_num_rows)
        self.sl_num_rows.valueChanged.connect(self.upd_sl_num_rows)
        self.sp_num_columns.valueChanged.connect(self.upd_sp_num_columns)
        self.sl_num_columns.valueChanged.connect(self.upd_sl_num_columns)
        self.sp_hgutter.valueChanged.connect(self.upd_sp_hgutter)
        self.sl_hgutter.valueChanged.connect(self.upd_sl_hgutter)
        self.sp_vgutter.valueChanged.connect(self.upd_sp_vgutter)
        self.sl_vgutter.valueChanged.connect(self.upd_sl_vgutter)
        b_color_gutter.clicked.connect(self.color_gutter_dialog)
        self.sp_outline.valueChanged.connect(self.upd_sp_outline)
        self.sl_outline.valueChanged.connect(self.upd_sl_outline)
        b_color_outline.clicked.connect(self.color_outline_dialog)"""

        self.window = QWidget(self)
        self.window.setLayout(mainLayout)
        self.scrollMainLayout.setWidget(self.window)
        self.setWidget(self.scrollMainLayout)
        self.show()
    """def __init__(self, ):
        super().__init__()
        #qt.QWidget.__init__(self)
        #self.setParent(parent, QtCore.Qt.Window)
        self.init_ui()"""

    def init_ui(self):
        self.setWindowTitle('Asset Manager')
        self.setGeometry(10,10,640,480)
        self.main_widget = qt.QWidget()
        button = qt.QPushButton("test")
        self.main_widget.setLayout(qt.QHBoxLayout())
        button.clicked.connect(self.close1)
        self.main_widget.layout().addWidget(button)
        """self.mainlayout = qt.QVBoxLayout()
        ##lines
        self.project_line = self.add_line_edit("Project : ", "")
        self.asset_line = self.add_line_edit("Asset : ", "")
        self.task_line = self.add_line_edit("Task : ", "")
        self.subtask_line = self.add_line_edit("Subtask : ", "")
        self.iteration_line = self.add_line_edit("Iteration : ", "")
        self.action_layout = qt.QHBoxLayout()
        self.save_button = qt.QPushButton("Save Asset11")
        self.save_button.clicked.connect(self.close1)
        self.action_layout.addWidget(self.save_button)
        #QtCore.Q
        #connect(self.save_button, QtCore.SIGNAL('clicked()'),self.close1)
        self.cancel_button = qt.QPushButton("Cancel Asset")
        self.cancel_button.clicked.connect(self.cancel)
        self.action_layout.addWidget(self.cancel_button)
        self.mainlayout.addLayout(self.action_layout)
        self.console = qt.QLabel("pfff")
        self.mainlayout.addWidget(self.console)
        self.mainlayout.addWidget(self.save_button)
        self.main_widget.setLayout(self.mainlayout)
        """
        self.setWidget(self.main_widget)
        self.show()

    def add_line_edit(self, label, value):
        layout = qt.QHBoxLayout()
        widget_name = qt.QLabel(label)
        layout.addWidget(widget_name)
        input_field = qt.QLineEdit(value)
        layout.addWidget(input_field)
        self.mainlayout.addLayout(layout)
        return input_field

    @pyqtSlot(bool)
    def close1(self, val):
        self.console.setText("Teeeeees")

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
