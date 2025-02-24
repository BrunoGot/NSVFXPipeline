import importlib
import sys

from PySide2.QtWidgets import QWidget, QApplication
from pipeline.tools.GUI import save_asset_gui as base_gui
importlib.reload(base_gui)


class HoudiniSaveUI(base_gui.SaveAssetGUI):
    def __init__(self, engine, scene_path=""):
        super(HoudiniSaveUI, self).__init__(engine, scene_path=scene_path)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = HoudiniSaveUI()
    sys.exit(app.exec_())
