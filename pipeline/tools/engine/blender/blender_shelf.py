import os

import bpy

from pipeline import fileSystem as fs
from pipeline.tools.engine import engine
from pipeline.tools.engine.blender import blender_engine, blender_save_ui

def save_asset(path):
    pass
    print("blender_shelf.save_asset")
    blender_save_ui.show_ui(blender_engine, scene_path=path)


if __name__ == "__main__":
    p = save_asset(r"D:\\Prod/03_WORK_PIPE/01_ASSET_3D\\Save_as\\Pipeline_Test\\Blender\\Deployment_Test\\001\\MandalaPower_007.blend")
    print("p = "+p)