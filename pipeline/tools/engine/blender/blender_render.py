import os

import bpy

from pipeline import fileSystem as fs

def update_render_path():
    """update the file path for render"""
    render_path = os.path.join(fs.asset_base_path,fs.get_render_path(bpy.data.filepath))
    os.makedirs(render_path, exist_ok=True)
    print(f"render âth = {render_path}")
    bpy.context.scene.render.filepath = render_path+"_"