import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, \
    QListWidgetItem, QLabel, QTextEdit


from pipeline.tools.Standalone.RenderQueueManager.controller.render_queue import RenderQueue
from pipeline.tools.Standalone.RenderQueueManager.view.render_settings_ui import RenderSettingsUI


class JobWidget(QWidget):
    on_remove_job = Signal(str)

    def __init__(self, job):
        super(JobWidget, self).__init__()
        self.job = job
        main_layout = QHBoxLayout()
        # id label
        main_layout.addWidget(QLabel(self.job.job_id))

        # scene path button
        scene_path_btn = QPushButton(self.job.scene_name)
        scene_path_btn.clicked.connect(lambda: self.open_folder(self.job.scene_path))
        main_layout.addWidget(scene_path_btn)

        # output folder path
        self._out_path_btn = QPushButton("Out Folder")
        self._out_path_btn.clicked.connect(lambda: self.open_folder(self.job.out_path))
        if not os.path.exists(os.path.dirname(self.job.out_path)):
            self._out_path_btn.setEnabled(False)
        main_layout.addWidget(self._out_path_btn)

        #status button
        self._status_btn = QPushButton(self.job.status.name)
        main_layout.addWidget(self._status_btn)

        # settings button
        self._setting_btn = QPushButton("S")
        self._setting_btn.clicked.connect(self.on_render_settings_clicked)
        main_layout.addWidget(self._setting_btn)

        # progress bar
        # viewer
        # remove button
        self._remove_job_btn = QPushButton("X")
        self._remove_job_btn.clicked.connect(self.remove_job)
        main_layout.addWidget(self._remove_job_btn)

        self.setLayout(main_layout)
        self.render_settings_view = RenderSettingsUI(self.job)

    def on_render_settings_clicked(self):
        #display view with job settings
        self.render_settings_view.show()
        print("display render settings view")


    def open_folder(self, path):
        os.startfile(os.path.dirname(path)) #this wont work for out_put folder when the subfolder bug will be fixed

    def remove_job(self):
        print(self.job.job_id)
        self.on_remove_job.emit(self.job.job_id)