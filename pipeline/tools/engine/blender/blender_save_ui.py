import os
import sys

from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, \
    QPushButton, QTreeView, QLayout
from PySide2.QtGui import QStandardItem, QStandardItemModel


class BlenderSaveUI(QWidget):
    def __init__(self):
        super(BlenderSaveUI, self).__init__()
        self.project_structure = {}

        # GUI panel
        main_layout = QVBoxLayout()
        info_panel = QHBoxLayout()
        left_panel = QVBoxLayout()
        left_panel.addLayout(self.add_pipeline_folder("Project"))
        left_panel.addLayout(self.add_pipeline_folder("Name"))
        left_panel.addLayout(self.add_pipeline_folder("Task"))
        left_panel.addLayout(self.add_pipeline_folder("Subtask"))
        left_panel.addLayout(self.add_pipeline_folder("Version"))
        info_panel.addLayout(left_panel)

        # treeview
        tree_view = QTreeView()
        tree_model = QStandardItemModel()
        tree_model = self.fill_tree_view(tree_model)
        tree_view.setModel(tree_model)
        tree_view.setMinimumSize(100,300)
        info_panel.addWidget(tree_view)
        main_layout.addLayout(info_panel)
        # comments
        main_layout.addWidget(QLabel("comment"))
        comment_box = QTextEdit()
        comment_box.setMaximumHeight(75)
        main_layout.addWidget(comment_box)
        # btn layouts
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        button_layout.addWidget(save_btn)
        cancel_btn = QPushButton("Cancel")
        button_layout.addWidget(cancel_btn)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.show()

    def add_node(self, parent_path, list_elem):
        nodes = []
        for e in list_elem:
            node = QStandardItem()
            node.setText(e)
            path = os.path.join(parent_path, e)
            if os.path.isdir(path):
                childrens = os.listdir(path)
                node.appendRows(self.add_node(path, childrens))
            nodes.append(node)
        return nodes

    def fill_tree_view(self, tree_model):
        types_folder = os.listdir(r'D:/Prod/03_WORK_PIPE/01_ASSET_3D') #fs.asset_base_path)
        root_node = tree_model.invisibleRootItem()
        root_node.appendRows(self.add_node(r'D:/Prod/03_WORK_PIPE/01_ASSET_3D', types_folder))#fs.asset_base_path, types_folder))
        return tree_model

    def add_pipeline_folder(self, label_name):
        layout = QHBoxLayout()
        project_label = QLabel(label_name)
        layout.addWidget(project_label)
        project_line_edit = QLineEdit()
        layout.addWidget(project_line_edit)
        self.project_structure[label_name] = project_line_edit
        return layout


def show_ui():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = BlenderSaveUI()
    app.exec_()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = BlenderSaveUI()
    #sys.exit(app.exec_())
