"""SaveConceptGUI is the actual gui for krita"""
import os

from krita import *

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, \
    QPushButton, QTreeView
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from pipeline.tools.GUI.save_asset_gui import SaveAssetGUI

"""todo: faire une classe mere save asset, faire derriver SaveConceptGUI et Save_asset de cette classe """

class KritaSaveUI(DockWidget, SaveAssetGUI):
    def __init__(self, engine, scene_path=""):
        super(KritaSaveUI, self).__init__(engine, scene_path=scene_path)
        QWidget.__init__(self)
        self.window = QWidget(self)
        self.window.setLayout(self.main_layout)
        self.setWidget(self.window)
        self.show()

    def tree_node_clicked(self, item):
        print(f"QStandardItem = {item.parent()}")
        # current_depth = self.get_depth_node(item)
        parent_list = [item.text()]
        parent_list += self.get_parent_list(item)
        path = os.path.join(*reversed(parent_list))
        print(f"path = {path}")
        self.current_selected_path = os.path.join(self.base_path, path)
        print(f"new_node_path = {self.current_selected_path}")
        if os.path.isdir(self.current_selected_path):
            # self.current_selected_path = new_node_path
            nodes = self.add_node(self.current_selected_path, os.listdir(self.current_selected_path))
            item.appendRows(nodes)
        self.tree_view.viewport().update()
        self.tree_view.setExpanded(self.tree_model.indexFromItem(item), True)

        self.fill_asset_form(parent_list)

    def fill_asset_form(self, parent_list):
        i = 1
        for line_edit in self.project_structure.values():
            if len(parent_list) >= i:
                line_edit.setText(parent_list[-i])
                i += 1
            else:
                break

    def get_parent_list(self, node):
        """
        recursive function to get the list of parents of the node item
        :param QStandardItem node:
        :return str[]: list of node in parents
        """
        parents = []
        parent = node.parent()
        if parent is not None:
            parents.append(parent.text())
            parents.extend(self.get_parent_list(parent))
        return parents

    def add_node(self, parent_path, list_elem):
        nodes = []
        for e in list_elem:
            node = QStandardItem()
            node.setText(e)
            path = os.path.join(parent_path, e)
            if os.path.isdir(path):
                pass
                # childrens = os.listdir(path)
                # node.appendRows(self.add_node(path, childrens))
            nodes.append(node)
        return nodes

    def fill_tree_view(self, tree_model):
        types_folder = os.listdir(self.current_selected_path)  # fs.asset_base_path)
        root_node = tree_model.invisibleRootItem()
        root_node.appendRows(
            self.add_node(self.current_selected_path, types_folder))  # fs.asset_base_path, types_folder))
        return tree_model

    def add_pipeline_folder(self, label_name):
        layout = QHBoxLayout()
        project_label = QLabel(label_name)
        layout.addWidget(project_label)
        project_line_edit = QLineEdit()
        layout.addWidget(project_line_edit)
        self.project_structure[label_name] = project_line_edit
        return layout

    def on_save(self):
        for i, j in self.project_structure.items():
            self.datas[i] = j.text()
        self.engine.save(self.datas)
        self.close()

    def on_close(self):
        self.close()

