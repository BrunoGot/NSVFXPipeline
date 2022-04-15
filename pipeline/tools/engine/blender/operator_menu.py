#here are the core function of the menu
lib_path = r"D:\Documents\Code\Python\NSVFXPipeline"
lib_path_pipeline = r"D:\Documents\Code\Python\NSVFXPipeline\pipeline"
lucidity_path = r"C:\Users\Natspir\PycharmProjects\AssetManager\venv\Lib\site-packages"
import sys

if lib_path not in sys.path:
    sys.path.append(lib_path)
    sys.path.append(lib_path_pipeline)

if lucidity_path not in sys.path:
    sys.path.append(lucidity_path)

import bpy
import importlib
from pipeline import *
from pipeline.tools.engine.blender import blender_shelf as shelf
from pipeline.tools.engine import engine

importlib.reload(shelf)
importlib.reload(engine)

    
###################
######Save As######
###################
class MenuSaveOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "pipeline_menu.save_as"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        self.save_asset(context)
        return {'FINISHED'}
    
    def save_asset(self,context):
        print("youpi")
        #asset_gui =#SaveAssetGUI("Test", self.save_callback) 
        path = bpy.data.filepath
        p = shelf.save_asset(path)
        print("p = "+p)
        if p:
            bpy.ops.wm.save_as_mainfile(filepath=p)
        #asset_gui.show()
        
###################
######Open file######
###################
class MenuOpenOperator(bpy.types.Operator):
    bl_idname = "pipeline_menu.open"
    bl_label = "Open file operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        self.explore_file()
        return {'FINISHED'}
    
    def explore_file(self):
        engine.explore_file(bpy.path.abspath("//"))

################################



def register():
    bpy.utils.register_class(MenuSaveOperator)
    bpy.utils.register_class(MenuOpenOperator)


def unregister():
    bpy.utils.unregister_class(MenuSaveOperator)


if __name__ == "__main__":
    register()
    print("test")
    #engine.save_as_asset("Test","Test","Test","Test","Test")
    # test call
    #bpy.ops.pipeline_menu.save_as()

