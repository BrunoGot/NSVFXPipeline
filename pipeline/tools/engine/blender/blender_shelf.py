import os

import bpy

from pipeline import fileSystem as fs
from pipeline.tools.engine import engine
from pipeline.tools.engine.blender import blender_engine, blender_save_ui
from pipeline.tools.engine.blender.blender_save_ui import BlenderSaveUI

def save_asset(path):
    pass
    print("ttessst")
    """window_ui = blender_save_ui.BlenderSaveUI(blender_engine)
    window_ui.show()"""
    blender_save_ui.show_ui(blender_engine)


if __name__ == "__main__":
    p = save_asset(r"D:\\Prod/03_WORK_PIPE/01_ASSET_3D\\Save_as\\Pipeline_Test\\Blender\\Deployment_Test\\001\\MandalaPower_007.blend")
    print("p = "+p)