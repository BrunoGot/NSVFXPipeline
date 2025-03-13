from importlib import reload

import bpy

from pipeline.tools.Standalone.RenderQueueManager.controller import render_queue as r

reload(r)

bl_info = {
    "name": "Render Queue Panel",
    "blender": (3, 0, 0),
    "category": "Render",
    "author": "Bruno Got",
    "version": (1, 0),
    "description": "Adds panel in the Output section to add the current scene in a render queue",
    "location": "Properties > Output",
    "warning": "",
    "support": "COMMUNITY",
}


class BlenderRenderQueuePanel(bpy.types.Panel):
    """
    create a custom panel in the output section. Have to be in the addon blender path to be loaded
    """
    bl_label = "Render Manager"
    bl_idname = "NS_RENDER_MANAGER"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Render Queue Manager")
        # set button
        layout.operator("wm.create_blender_job", text="Add to Render Queue")


class CreateBlenderJob(bpy.types.Operator):
    """
    Get the scene information from blender context to create the Job
    """

    bl_idname = "wm.create_blender_job"
    bl_label = "Create Blender Job"

    def execute(self, context):
        # 1 pack dependencies and
        # 2 save it as a renderfile here

        render_manager = r.RenderQueue()
        scene_path = bpy.data.filepath
        output_path = bpy.context.scene.render.filepath

        render_manager.register_job(scene_path, output_path)
        print("woooorks")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(BlenderRenderQueuePanel)
    bpy.utils.register_class(CreateBlenderJob)


def unregister():
    bpy.utils.unregister_class(BlenderRenderQueuePanel)
    bpy.utils.unregister_class(CreateBlenderJob)


if __name__ == "__main__":
    register()
