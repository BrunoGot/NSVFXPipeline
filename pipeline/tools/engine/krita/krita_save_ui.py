"""save window for krita"""

from krita import *

from PyQt5.QtWidgets import QWidget

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

