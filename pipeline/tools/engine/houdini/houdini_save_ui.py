import os
import sys

from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, \
    QPushButton, QTreeView, QLayout
from PySide2.QtGui import QStandardItem, QStandardItemModel

from pipeline import fileSystem as fs

from pipeline.tools.GUI.save_asset_gui import SaveAssetGUI

class HoudiniSaveUI(SaveAssetGUI):
    def __init__(self, engine, scene_path=""):
        super(HoudiniSaveUI, self).__init__(engine, scene_path=scene_path)


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = HoudiniSaveUI()
    sys.exit(app.exec_())
