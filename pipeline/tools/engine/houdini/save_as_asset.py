import importlib
import hou

from pipeline.tools.engine.houdini import houdini_engine
from pipeline import fileSystem as fs
from pipeline.tools.engine.houdini import houdini_save_ui
importlib.reload(houdini_save_ui)


def run():
    scene_path = hou.hipFile.path()
    w = houdini_save_ui.HoudiniSaveUI(houdini_engine, scene_path=scene_path)
    w.show()

if __name__ == "__main__":
    run()
