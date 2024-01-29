import os
import sys

from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, \
    QPushButton, QTreeView, QLayout
from PySide2.QtGui import QStandardItem, QStandardItemModel

from pipeline import fileSystem as fs

from pipeline.tools.GUI.save_asset_gui import SaveAssetGUI
class BlenderSaveUI(SaveAssetGUI):
    def __init__(self, engine, scene_path=""):
        super(BlenderSaveUI, self).__init__(engine, scene_path=scene_path)
        self.setLayout(self.main_layout)

def show_ui(engine, scene_path=""):
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = BlenderSaveUI(engine, scene_path=scene_path)
    w.show()
    app.exec_()
    print(f"datas = {w.datas}")
    return w.datas


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = BlenderSaveUI()
    sys.exit(app.exec_())
