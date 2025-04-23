import json
import os.path

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QListWidget, \
    QListWidgetItem, QLabel, QTextEdit, QFormLayout, QLineEdit, QSpinBox, QComboBox


class RenderSettingsUI(QWidget):
    def __init__(self, job):
        super(RenderSettingsUI, self).__init__()
        #attributes & config
        self.job = job
        self.preset_folder = os.path.join(os.path.abspath("."),"model","presets")
        # f"..\\model\\Presets"
        # ui
        self.main_layout = QVBoxLayout()
        self.settings_layout = QFormLayout()
        # Label
        title_label = QLabel(job.scene_name)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        # Form
        self.start_frame = QSpinBox()
        self.start_frame.setRange(0,10000)
        self.end_frame = QSpinBox()
        self.end_frame.setRange(0,10000)
        self.step_frame = QSpinBox()
        self.step_frame.setRange(0,10000)
        self.scale_resolution = QSpinBox()
        self.scale_resolution.setRange(0,10000)
        self.frame_rate = QSpinBox()
        self.presets = QComboBox()
        self.presets.addItems(["Custom", "Full", "Preview"])
        self.presets.currentTextChanged.connect(self.on_presets_loaded)
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
        self.main_layout.addWidget(QLabel("If all is set to 0,"
                                          " the render settings are took from the blender scene"))
        # [Cancel|Save] btn
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

    @property
    def preset_path(self):
        return os.path.join(self.preset_folder, f"{self.presets.currentText()}.json")

    def on_presets_loaded(self):
        preset_name = self.presets.currentText()
        if preset_name != "Custom":
            with open(self.preset_path, "r") as f:
                preset = json.load(f)
                self.set_input_values(start_frame=preset["frame_sequence"][0],
                                      end_frame=preset["frame_sequence"][1],
                                      step_frame=preset["frame_sequence"][2],
                                      resolution_scale=preset["pixel_size"][2],
                                      file_format=preset["file_format"],
                                      frame_rate=preset["frame_rate"])
                print(preset)

    def set_input_values(self, start_frame=0, end_frame=0, step_frame=0, resolution_scale=0, file_format="", frame_rate=0):
        """by giving the value in parameter, set the value on the user input"""
        self.start_frame.setValue(start_frame)
        self.end_frame.setValue(end_frame)
        self.step_frame.setValue(step_frame)
        self.scale_resolution.setValue(resolution_scale)
        self.file_format.setCurrentText(file_format)
        self.frame_rate.setValue(frame_rate)

    def is_input_valids(self):
        """
        check if the user input are corresponding to the rules.
        Here inputs are invalid if they all corresponding to 0
        """
        valid = True
        return not (self.scale_resolution.value() \
               == self.start_frame.value() \
               == self.end_frame.value() \
               == self.step_frame.value() \
               == self.frame_rate.value() == 0)

    def save_render_settings(self):
        # override job render settings here
        if self.is_input_valids():
            pixel_size = [1920, 1080, self.scale_resolution.value()]
            frame_sequence = [self.start_frame.value(), self.end_frame.value(), self.step_frame.value()]
            file_format = "png"
            frame_rate = self.frame_rate.value()
            self.job.set_render_settings({"pixel_size": pixel_size,
                                          "frame_sequence": frame_sequence,
                                          "file_format": file_format,
                                          "frame_rate": frame_rate})
            print("render settings have been overiden")
        else:
            print("All values = 0, no render settings have been overiden")

        self.close()
