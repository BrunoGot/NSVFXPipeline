import sys

from PySide2.QtWidgets import QApplication

from pipeline.tools.Standalone.RenderQueueManager.view.render_queue_ui import RenderQueueUI

def GUI_Style(app):
    file_qss = open("view/styles/Combinear.qss")
    with file_qss:
        qss = file_qss.read()
        app.setStyleSheet(qss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI_Style(app)
    ui = RenderQueueUI()
    ui.show()
    sys.exit(app.exec_())

