# GUI part of the menu
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
    bpy.ops.wm.call_menu(name=customMenu.bl_idname)

def unregister():
    bpy.utils.unregister_class(customMenu)


if __name__ == "__main__":
    register()