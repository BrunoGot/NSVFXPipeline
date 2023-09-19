import os
import importlib
import subprocess
import sys
import hou

from pipeline.tools.engine.houdini import houdini_engine
from pipeline import fileSystem as fs
from pipeline.tools.engine.houdini import houdini_save_ui
importlib.reload(houdini_save_ui)


def run():
    w = houdini_save_ui.BlenderSaveUI(houdini_engine)
    w.show()

if __name__ == "__main__":
    run()
