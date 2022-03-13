import os
import sys

import PyQt6.QtGui
import lucidity.error
from PyQt6 import QtWidgets, QtGui,QtCore
import argparse
from multiprocessing import Process, Pipe

##pipeline libs##
path = r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline'
if path not in sys.path:
    sys.path.append(path)
from pipeline.tools.engine import engine
from pipeline import fileSystem as fs
from pipeline.tools.GUI import custom_elements as NsGui
#################

class SaveAssetGUI(QtWidgets.QWidget):
    def __init__(self, ):
        QtWidgets.QWidget.__init__(self)

        #parsing arguments
        parser = argparse.ArgumentParser(description = "Save asset")
        parser.add_argument('--path', dest='path', type=str, help='path of the current asset to save')
        parser.add_argument('--ext', dest='ext', type=str, help='extension of the asset file')
        args = parser.parse_args()
        print("args = "+str(args.path))
        self.asset_path = args.path
        self.asset_ext = args.ext
        print("ext = " + self.asset_ext)

        #normalize the path with only '/' path
        self.asset_path = self.asset_path.replace("\\\\","/")
        path = self.asset_path.replace(fs.asset_base_path + "/", "")
        print("path = " + path)
        datas = fs.get_datas_from_path(path)
        print("in datas = " + str(datas))

        if datas:
            self.asset_name = datas['AssetName']
            self.asset_type = datas['AssetType']
            self.asset_task = datas['Task']
            self.asset_subtask = datas['Subtask']
            self.asset_version = datas['Version']
        else :
            self.asset_type = "Concept"
            self.asset_task = ""
            self.asset_subtask = ""
            self.asset_version = "001"

        # creation de l'application
        self.target_path = fs.asset_base_path
        self.asset_input_fields = [] #list of input field to get assets datas [QlineEdit]
        self.asset_name = "Test"
        self.draw_gui()
        self.event_flag = False
        #print("init")


    def add_line_edit(self, label, value):
        layout = QtWidgets.QHBoxLayout()
        widget_name = QtWidgets.QLabel(label)
        layout.addWidget(widget_name)
        input_field = NsGui.NsQlineEdit(value)
        layout.addWidget(input_field)
        self.right_panel.addLayout(layout)
        return input_field

    def click_on_edit_line(self, id_line_edit):
        #reset target path
        self.target_path = fs.asset_base_path
        #assemble all value of the dictionary preceding the key
        for i in self.asset_input_fields:
            if(i.text() == id_line_edit.text()):
                break
            self.target_path = os.path.join( self.target_path,i.text())

        print("self.target_path  "+self.target_path )
        self.datas_Type = QtGui.QStandardItemModel()
        completer = self.update_autocompletion(self.datas_Type)
        id_line_edit.setCompleter(completer)
    def draw_gui(self):

        self.main_layout = QtWidgets.QHBoxLayout()
        #self.setGeometry(1000,50,100,200)
        self.right_panel = QtWidgets.QVBoxLayout()

        ##picture##
        self.image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\GUI\Resources\saveAsset_GUIdraw.png")
        #pixmap.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #pixmap.fill(QtCore.Qt.yellow)
        pixmap = pixmap.scaledToHeight(200)
        self.image.setPixmap(pixmap)
        self.right_panel.addWidget(self.image)
        ####
        self.open_asset_folder_btn = QtWidgets.QPushButton("Open Asset Folder")
        self.open_asset_folder_btn.clicked.connect(self.open_asset_folder)
        self.right_panel.addWidget(self.open_asset_folder_btn)
        #
        self.type_input = self.add_line_edit("Type : ", self.asset_type)
        self.asset_input_fields.append(self.type_input)
        #self.type_input.textEdited.connect(self.update_target_path)
        #self.datas_Type = QtGui.QStandardItemModel()
        #completer = self.update_autocompletion(self.datas_Type)
        #self.type_input.setCompleter(completer)
        self.type_input.clicked.connect(lambda: self.click_on_edit_line(self.type_input))

        self.name_input = self.add_line_edit("Asset name : ", self.asset_name)
        self.asset_input_fields.append(self.name_input)
        #self.name_input.textEdited.connect(self.update_target_path)
        #self.model2 = QtGui.QStandardItemModel()
        #completer = self.update_autocompletion(self.model2)
        #self.name_input.setCompleter(completer)
        #self.name_input = self.update_autocompletion(self.name_input)
        self.name_input.clicked.connect(lambda: self.click_on_edit_line(self.name_input))

        """self.model = QtGui.QStandardItemModel()
        self.completer = QtWidgets.QCompleter(self.model, self)
        self.model.appendRow(QtGui.QStandardItem("test"))
        self.type_input.setCompleter(self.completer)"""
        self.task_input =self.add_line_edit("Task : ", self.asset_task)
        self.asset_input_fields.append(self.task_input)
        #self.task_input.textEdited.connect(self.update_target_path)
        #self.update_autocompletion(self.task_input)
        self.task_input.clicked.connect(lambda: self.click_on_edit_line(self.task_input))

        self.subtask_input = self.add_line_edit("Subtask : ", self.asset_subtask)
        self.asset_input_fields.append(self.subtask_input)
        self.subtask_input.clicked.connect(lambda: self.click_on_edit_line(self.subtask_input))

        self.version_input = self.add_line_edit("Version : ", self.asset_version)
        self.asset_input_fields.append(self.version_input)
        self.version_input.clicked.connect(lambda: self.click_on_edit_line(self.version_input))

        self.console = QtWidgets.QLabel("")
        self.right_panel.addWidget(self.console)
        #buttons valid or cancel
        h_button_layout = QtWidgets.QHBoxLayout()
        button_validate = QtWidgets.QPushButton("Save")
        button_validate.clicked.connect(self.save)
        h_button_layout.addWidget(button_validate)
        button_cancel = QtWidgets.QPushButton("Cancel")
        button_cancel.clicked.connect(self.cancel)
        h_button_layout.addWidget(button_cancel)
        self.right_panel.addLayout(h_button_layout)
        self.main_layout.addLayout(self.right_panel)
        #left panel tree view
        self.left_panel = QtWidgets.QVBoxLayout()
        tree_view = QtWidgets.QTreeView()
        tree_model = QtGui.QStandardItemModel()
        tree_model = self.fill_tree_view(tree_model)
        tree_view.setModel(tree_model)
        if self.asset_type:
            pass
            #item = tree_view.findItems(self.asset_type)
            #print("item found : "+str(item))
        #tree_view.expandAll()
        self.left_panel.addWidget(tree_view)
        self.main_layout.addLayout(self.left_panel)
        self.setLayout(self.main_layout)

    def add_node(self, parent_path, list_elem):
        nodes = []
        for e in list_elem:
            node = QtGui.QStandardItem()
            node.setText(e)
            path = os.path.join(parent_path, e)
            if os.path.isdir(path):
                childrens = os.listdir(path)
                node.appendRows(self.add_node(path, childrens))
            nodes.append(node)
        return nodes

    def fill_tree_view(self, tree_model):
        types_folder = os.listdir(fs.asset_base_path)
        root_node = tree_model.invisibleRootItem()
        root_node.appendRows(self.add_node(fs.asset_base_path,types_folder))
        return tree_model

    def update_autocompletion(self,model ):
        print("self.target_path = "+self.target_path)
        #reinit the model
        if os.path.isdir(self.target_path):
            #get all element in path
            list_elem = os.listdir(self.target_path)
            list_dir = []
            #filter only folder in this path
            for e in list_elem:
                if os.path.isdir(os.path.join(self.target_path,e)):
                    list_dir.append(e)
            #convert it as items and add it to the model completer
            for d in list_dir:
                model.appendRow(QtGui.QStandardItem(d))

        completer = QtWidgets.QCompleter(model, self)

        return completer
        print("list_dir = "+  str(list_dir))

    def update_target_path(self,txt):
        self.target_path = os.path.join(self.target_path,txt)

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

    def get_path_id(self, name, type, task, subtask, version):
        asset_datas = {"AssetType": type, "AssetName": name, "Task": task, "Subtask": subtask, "Version": version, "ext":self.asset_ext}
        path_id = engine.make_asset_path(asset_datas)
        #asset_file_path = fs.conf.asset_file_name.format(asset_datas)
        path_id = os.path.join(path_id,fs.conf.asset_file_name.format(asset_datas))
        return path_id

    ###callbacks###
    def open_asset_folder(self):
        os.startfile(os.path.dirname(self.asset_path))

    def save(self):
        print("save")
        #check input value
        name = self.name_input.text()
        type = self.type_input.text()
        task = self.task_input.text()
        subtask = self.subtask_input.text()
        version = self.version_input.text()
        #if they are good :
        error_msg, check_value_flag = self.check_value(name, type, task, subtask, version)
        if check_value_flag is True:
            # configure path
            path = self.get_path_id(name, type, task, subtask, version)
            #print the path
            #print("save : name = {}, type = {}, task = {},subtask = {}, version = {}".format(name, type, task, subtask, version ))
            path = path.replace("\\","/")
            #path+="/"+name+"_"+version
            print("save path_id = "+ path)
            self.event_flag = True
            self.close()
        else: #print an error message
            self.console.setText(error_msg)

    def cancel(self):
        self.event_flag = False
        print("close")
        self.close()

def set_gui_style(app):
    print("file = "+__file__)
    file_qss = open(r"C:\Users\Natspir\PycharmProjects\AssetManager\View\Styles\Combinear.qss")
    with file_qss:
        qss = file_qss.read()
        #print("QSS = "+qss)
        app.setStyleSheet(qss)

def show_gui():
    print("show gui")
    app = QtWidgets.QApplication(sys.argv)
    set_gui_style(app)
    gui = SaveAssetGUI()
    gui.show()
    app.exec()

if __name__ == "__main__":
    #print("test")
    show_gui()
    """datas = {"AssetType": "type", "AssetName": "name", "Task": "task", "Subtask": "subtask", "Version": "version"}
    folder_path = fs.get_folder_path(datas)
    folder_path = os.path.join(folder_path,fs.conf.asset_file_name.format(datas))
    print("folder_path = "+folder_path)"""