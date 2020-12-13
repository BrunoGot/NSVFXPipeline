import os
import hou
from pipeline import framework_config as config


def load_shelves():
    custom_shelves_dir = config.get_pipeline_path()+os.sep+config.get_houdini_path() + "/houdini/shelves"

    current_shelves = hou.shelves.shelfSets()
    custom_shelves_dir = custom_shelves_dir.replace('/', os.sep)

    print("list des shelves : "+str(current_shelves))
    print("load shelf in "+custom_shelves_dir)
    shelves = os.listdir(custom_shelves_dir)
    for shelf in shelves:
        if ".shelf" in shelf:
            custom_shelf_path = custom_shelves_dir+os.sep+shelf
            hou.shelves.loadFile(custom_shelf_path)
    print("liste des custom shelves : "+str(shelf))
