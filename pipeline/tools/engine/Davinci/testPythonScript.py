print("yooooooo")

# Chat gpt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
import DaVinciResolveScript as dvr


def get_resolve():
    try:
        return dvr.scriptapp("Resolve")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Could not connect to DaVinci Resolve: {e}")
        return None


class ResolveShelf(QWidget):
    def __init__(self):
        super().__init__()
        self.resolve = get_resolve()
        if not self.resolve:
            sys.exit(1)

        self.project_manager = self.resolve.GetProjectManager()
        self.project = self.project_manager.GetCurrentProject()
        self.media_pool = self.project.GetMediaPool()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        btn_import = QPushButton("Import Media", self)
        btn_import.clicked.connect(self.import_media)
        layout.addWidget(btn_import)

        btn_create_timeline = QPushButton("Create New Timeline", self)
        btn_create_timeline.clicked.connect(self.create_timeline)
        layout.addWidget(btn_create_timeline)

        btn_render = QPushButton("Render Timeline", self)
        btn_render.clicked.connect(self.render_timeline)
        layout.addWidget(btn_render)

        self.setLayout(layout)
        self.setWindowTitle("DaVinci Resolve Shelf")
        self.resize(300, 150)

    def import_media(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Media Files", "",
                                                "Video Files (*.mp4 *.mov *.avi);;All Files (*)")
        if files:
            self.media_pool.ImportMedia(files)
            QMessageBox.information(self, "Success", "Media imported successfully!")

    def create_timeline(self):
        timeline_name = "New Timeline"
        if self.media_pool.CreateEmptyTimeline(timeline_name):
            QMessageBox.information(self, "Success", "New timeline created!")
        else:
            QMessageBox.warning(self, "Error", "Failed to create timeline.")

    def render_timeline(self):
        if not self.project:
            QMessageBox.warning(self, "Error", "No active project.")
            return

        self.project.SetRenderSettings({
            "TargetDir": "~/Desktop/",
            "CustomName": "Rendered_Project",
            "Format": "mp4",
        })

        if self.project.StartRendering():
            QMessageBox.information(self, "Rendering", "Rendering started!")
        else:
            QMessageBox.warning(self, "Error", "Could not start rendering.")


if __name__ == "__main__":
    print("in main")
    app = QApplication(sys.argv)
    shelf = ResolveShelf()
    shelf.show()
    sys.exit(app.exec_())
