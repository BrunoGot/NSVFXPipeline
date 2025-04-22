from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, \
    QListWidgetItem, QLabel, QTextEdit, QFormLayout, QLineEdit, QSpinBox, QComboBox

class RenderSettingsUI(QWidget):
    def __init__(self, job):
        super(RenderSettingsUI, self).__init__()

        self.job = job
        #ui
        self.main_layout = QVBoxLayout()
        self.settings_layout = QFormLayout()
        #Label
        title_label = QLabel(job.scene_name)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        #Form
        self.start_frame = QSpinBox()
        self.end_frame = QSpinBox()
        self.step_frame = QSpinBox()
        self.scale_resolution = QSpinBox()
        self.frame_rate = QSpinBox()
        self.presets = QComboBox()
        self.presets.addItems(["Custom", "Full", "Preview"])
        self.file_format = QComboBox()
        self.file_format.addItems(["png", "jpg", "mov", "exr"])
        self.settings_layout.addRow("Presets:", self.presets)
        self.settings_layout.addRow("Start Frame:", self.start_frame)
        self.settings_layout.addRow("End Frame:", self.end_frame)
        self.settings_layout.addRow("Step Frame:", self.step_frame)
        self.settings_layout.addRow("Resolution Scale:", self.scale_resolution)
        self.settings_layout.addRow("file format:", self.file_format)
        self.settings_layout.addRow("frame rate format:", self.frame_rate)
        self.main_layout.addLayout(self.settings_layout)
        #[Cancel|Save] btn
        btn_layout = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        btn_layout.addWidget(cancel_btn)
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_render_settings)
        btn_layout.addWidget(save_btn)

        self.main_layout.addLayout(self.settings_layout)
        self.main_layout.addLayout(btn_layout)

        self.setLayout(self.main_layout)

    def save_render_settings(self):
        #override job render settings here
        pixel_size = [1920,1080,self.scale_resolution.value()]
        frame_sequence = [self.start_frame.value(),self.end_frame.value(),self.step_frame.value()]
        file_format = "png"
        frame_rate = 30
        self.job.set_render_settings({"pixel_size": pixel_size,
                                      "frame_sequence": frame_sequence,
                                      "file_format": file_format,
                                      "frame_rate": frame_rate})
        self.close()