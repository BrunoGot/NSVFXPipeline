# list all the dependencies of a blender file

import bpy


def get_dependencies():
    """
    list all dependencies of the blender scene that execute this code
    :return: dictionary "dependencies {name : [class, filepath]}
    """
    dependencies = {}  # name : [class, filepath]
    cls = type(bpy.data.objects)
    for attr in dir(bpy.data):
        collections = getattr(bpy.data, attr)
        # print(f"bpy.collections = {collections}")
        if isinstance(collections, cls):
            for data_block in collections:
                # print(f'[{data_block.__class__}] {data_block.name} :  ')

                if hasattr(data_block, "filepath") and data_block.filepath:
                    print(f'[{data_block.__class__}] :  {data_block.filepath}')
                    dependencies[data_block.name] = [data_block.__class__, data_block.filepath]
                    print("--------")
    return dependencies

if __name__ == "__main__":
    print("lunch python")
    get_dependencies()