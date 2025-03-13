import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow,QVBoxLayout,QHBoxLayout, QWidget, QPushButton, QListWidget,\
    QListWidgetItem, QLabel


from pipeline.tools.Standalone.RenderQueueManager.controller.render_queue import RenderQueue

class JobWidget(QWidget ):
    on_remove_job = Signal(str)

    def __init__(self, job):
        super(JobWidget, self).__init__()
        self.job = job
        main_layout = QHBoxLayout()
        #id label
        main_layout.addWidget(QLabel(self.job.job_id))
        #scene path button
        scene_path_btn = QPushButton(self.job.scene_name)
        scene_path_btn.clicked.connect(self.open_folder)
        main_layout.addWidget(scene_path_btn)
        #remove button
        self.remove_job_btn = QPushButton("X")
        self.remove_job_btn.clicked.connect(self.remove_job)
        main_layout.addWidget(self.remove_job_btn)

        self.setLayout(main_layout)

    def open_folder(self):
        os.startfile(os.path.dirname(self.job.scene_path))

    def remove_job(self):
        print(self.job.job_id)
        self.on_remove_job.emit(self.job.job_id)

class RenderQueueUI(QMainWindow):

    def __init__(self):
        super(RenderQueueUI, self).__init__()
        self.render_manager = RenderQueue()
        self.render_manager.on_update_view.connect(self.update_view)
        self.init_UI()

    def init_UI(self):
        main_widget = QWidget()
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

        #row


        main_widget.setLayout(self.v_layout)
        self.setCentralWidget(main_widget)

    def _create_job_list_widget(self):
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
        print("update viewww")