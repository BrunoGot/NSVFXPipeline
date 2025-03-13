import os

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, \
    QListWidgetItem, QLabel, QTextEdit


from pipeline.tools.Standalone.RenderQueueManager.controller.render_queue import RenderQueue


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

        # remove button
        self._remove_job_btn = QPushButton("X")
        self._remove_job_btn.clicked.connect(self.remove_job)
        main_layout.addWidget(self._remove_job_btn)

        self.setLayout(main_layout)

    def open_folder(self, path):
        os.startfile(os.path.dirname(path)) #this wont work for out_put folder when the subfolder bug will be fixed

    def remove_job(self):
        print(self.job.job_id)
        self.on_remove_job.emit(self.job.job_id)


class RenderQueueUI(QMainWindow):

    def __init__(self):
        super(RenderQueueUI, self).__init__()
        self.render_manager = RenderQueue()
        self.render_manager.on_update_view.connect(self.update_view)
        self.render_manager.on_steam_updated.connect(self.update_output_stream_view)
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

        self.job_stream_output = QTextEdit()
        self.v_layout.addWidget(self.job_stream_output)

        # row

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

    def update_output_stream_view(self, std, err):

        self.job_stream_output.append(std)
        if err:
            self.job_stream_output.append(f'<span style="color: red;">{err}</span>')
