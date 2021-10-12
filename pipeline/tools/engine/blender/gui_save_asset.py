import sys
from Qt import QtWidgets

"""class SaveAssetGUI():
    def __init__(self):
        pass


"""
class SaveAssetGUI:

    def __init__(self, file_name, save_callback):
        self.asset_name = file_name
        self.asset_coords = {} #datas of the recorded asset
        self.main_layout = QtWidgets.QVBoxLayout()
        self.save_callback = save_callback

    def add_line_edit(self, label, value):
        widget_name = QtWidgets.QLabel(label)
        self.main_layout.addWidget(widget_name)
        input_field = QtWidgets.QLineEdit(value)
        self.main_layout.addWidget(input_field)
        return input_field


    def gui(self):
        """label_asset_name = QtWidgets.QLabel("Asset name : ")
        main_layout.addWidget(label_asset_name)
        input_asset_name = QtWidgets.QLineEdit(self.asset_name)"""
        self.name_input = self.add_line_edit("Asset name : ", self.asset_name)
        self.type_input = self.add_line_edit("Type : ", self.asset_name)
        self.task_input =self.add_line_edit("Task : ", self.asset_name)
        self.subtask_input = self.add_line_edit("Subtask : ", self.asset_name)
        self.version_input = self.add_line_edit("Version : ", "001")

        #buttons valid or cancel
        h_button_layout = QtWidgets.QHBoxLayout()
        button_validate = QtWidgets.QPushButton("Save")
        button_validate.clicked.connect(self.save)
        h_button_layout.addWidget(button_validate)
        button_cancel = QtWidgets.QPushButton("Cancel")
        button_cancel.clicked.connect(self.cancel)
        h_button_layout.addWidget(button_cancel)
        self.main_layout.addLayout(h_button_layout)
        return self.main_layout


    def save(self):
        name = self.name_input.text()
        type = self.type_input.text()
        task = self.task_input.text()
        subtask = self.subtask_input.text()
        version = self.version_input.text()
        self.asset_coords = {"AssetType" : name, "AssetName": type, "Task" : task, "Subtask": subtask, "Version" : version}
        #print("saving "+self.asset_coords["name"])
        self.save_callback(self.asset_coords)
        self.cancel()

    def cancel(self):
        print("cancel")
        self.app.quit()

    def show(self):
        #creation de l'application
        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        #creation de la fenetre
        self.mainWindow = QtWidgets.QDialog()

        main_layout = self.gui()
        self.mainWindow.setLayout(main_layout)

        self.mainWindow.show()
        #"""
        #button = QtWidgets.QPushButton("Hello bande de batard !!")
        #button.show()
        #"""
        self.app.exec_()
#"""

def test():
    print("test")
    import subprocess
    path_file = r"C:\\Users\\Natspir\\NatspirProd\\03_WORK_PIPE\\01_ASSET_3D\\Concept\\MandalaPower\\Psyched\\Base\\006\\MandalaPower_006.kra"
    p = subprocess.Popen([r'C:\\Users\\Natspir\\Documents\\Code\\Python\\AssetManager\\venv\\Scripts\\Python.exe',
                          r'C:\\Users\\Natspir\\Documents\\Code\\Python\\NSVFXPipeline\\pipeline\\tools\\GUI\\save_asset_gui.py',
                          '--path=' + path_file, '--ext=kra'], shell=True, stdout=subprocess.PIPE)

if __name__ == "__main__":
    testGui = SaveAssetGUI("test", test)
    testGui.show()
