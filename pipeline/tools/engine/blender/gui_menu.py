bl_info = {
    "name": "NSVFXPipeline",
    "author": "Natspir !!",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D Viewport",
    "description": "NSVFXPipeline shelf for blender",
    "warning": "",
    "doc_url": "",
    "category": "Interface"
}


#-------------operator menu part------------#
#here are the core function of the menu
lib_path = r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline"
lib_path_pipeline = r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline"
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



#-----------------------------------------#




# GUI part of the context menu

import bpy

class customMenu(bpy.types.Menu):
    bl_label = "custom menu"
    bl_idname = "view3D.custom_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_cube_add", text="test")
        layout.operator("pipeline_menu.save_as", text="Save File")
        layout.operator("pipeline_menu.open", text="Open File")

    @property
    def test():
        print("woorks")

def register():
    bpy.utils.register_class(customMenu)
    bpy.utils.register_class(MenuSaveOperator)
    bpy.utils.register_class(MenuOpenOperator)
    #bpy.ops.wm.call_menu(name=customMenu.bl_idname)

def unregister():
    bpy.utils.unregister_class(customMenu)


if __name__ == "__main__":
    register()
    