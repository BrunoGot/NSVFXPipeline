import sys

from PySide2.QtWidgets import QApplication

from pipeline.tools.Standalone.RenderQueueManager.view.render_queue_ui import RenderQueueUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = RenderQueueUI()
    ui.show()
    sys.exit(app.exec_())

