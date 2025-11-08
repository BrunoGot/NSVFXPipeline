import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, \
    QListWidgetItem, QLabel, QTextEdit


from pipeline.tools.Standalone.RenderQueueManager.controller.render_queue import RenderQueue
from pipeline.tools.Standalone.RenderQueueManager.view.job_widget_ui import JobWidget



class RenderQueuePanel(QWidget):
    def __init__(self):
        super(RenderQueuePanel, self).__init__()
        self.render_manager = RenderQueue()
        self.render_manager.on_update_view.connect(self.update_view)
        self.render_manager.on_steam_updated.connect(self.update_output_stream_view)
        self.init_UI()

    def init_UI(self):
        self.setMinimumWidth(800)
        self.v_layout = QVBoxLayout()

        self.list_widget = QListWidget(self)
        self._create_job_list_widget()

        self.v_layout.addWidget(self.list_widget)

        self.update_btn = QPushButton("Update")
        self.update_btn.clicked.connect(self.update_view)
        self.v_layout.addWidget(self.update_btn)

        self.execute_button = QPushButton("Execute")
        self.execute_button.clicked.connect(self.render_manager.execute)
        self.v_layout.addWidget(self.execute_button)

        self.job_stream_output = QTextEdit()
        self.v_layout.addWidget(self.job_stream_output)

        # row

        self.setLayout(self.v_layout)

    def _create_job_list_widget(self):
        """
        for all jobs in the render_manager model create the associated UI Widget
        :return:
        """
        for job in self.render_manager.jobs:
            id = job.job_id
            job_widget = JobWidget(job)
            job_widget.on_remove_job.connect(self.render_manager.remove_job)
            item = QListWidgetItem(self.list_widget)
            item.setSizeHint(job_widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, job_widget)

    def update_view(self):
        self.render_manager.refresh_job_list()
        self.list_widget.clear()
        self._create_job_list_widget()

    def update_output_stream_view(self, std, err):

        self.job_stream_output.append(std)
        if err:
            self.job_stream_output.append(f'<span style="color: red;">{err}</span>')