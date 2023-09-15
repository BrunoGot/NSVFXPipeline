import os

import bpy

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs
from pipeline.tools.engine.blender import blender_render

def save(asset_datas):
    # asset_datas = engine.save_asset(path)  # save_asset() should be named other like get asset_datas
    print("asset_datas = {}".format(asset_datas))
    ###todo:should go into a new save_asset method from engine, this code can be merged with houdiniengine.save###
    if asset_datas:
        if "ext" not in asset_datas:
            asset_datas["ext"] = "blend"  # blend should be a parameter
        base_path = engine.make_asset_path(asset_datas)
        path_id = os.path.join(base_path, fs.conf.asset_file_name.format(asset_datas))
        print("path_id = {}".format(path_id))
    print("path ready to save = {}".format(path_id))
    ###
    if not on_save_handlers in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.append(on_save_handlers)
    bpy.ops.wm.save_as_mainfile(filepath=path_id)
    blender_render.update_render_path()
    print(f"saved as {path_id} ")

    return path_id


def on_save_handlers(scene):
    blender_render.update_render_path()
    print("on save trigged scene = {}".format(scene))