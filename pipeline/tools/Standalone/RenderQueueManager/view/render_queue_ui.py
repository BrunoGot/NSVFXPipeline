import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, \
    QListWidgetItem, QLabel, QTextEdit


from pipeline.tools.Standalone.RenderQueueManager.view.render_queue_panel_ui import RenderQueuePanel


class RenderQueueUI(QMainWindow):
    def __init__(self):
        super(RenderQueueUI, self).__init__()
        self.render_queue_panel = RenderQueuePanel()
        self.setCentralWidget(self.render_queue_panel)

