from krita import Krita, Extension


class SimplePlugin(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("simple_plugin_action", "Simple Plugin Action", "tools/scripts")
        action.triggered.connect(self.runPlugin)

    def runPlugin(self):
        app = Krita.instance()
        active_doc = app.activeDocument()

        if active_doc:
            # Your plugin logic goes here
            active_node = active_doc.activeNode()
            print(f"Running the plugin on document '{active_doc.name()}' and node '{active_node.name()}'")


if __name__ == "__main__":
    # Register the plugin
    app = Krita.instance()
    plugin = SimplePlugin(app)
    app.addExtension(plugin)
