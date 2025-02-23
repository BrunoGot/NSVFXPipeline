import os
from pathlib import Path
import hou

from pipeline import framework_config as config


def load_shelf():
    shelf_path = r"/houdini/settings/shelves/"
    pipeline_shelf_path = config.get_framework_path()+os.path.sep+config.get_houdini_path()+os.path.sep+shelf_path+os.path.sep+"NSPipeline.shelf"
    pipeline_shelfSet = config.get_framework_path()+os.path.sep+config.get_houdini_path()+os.path.sep+shelf_path+os.path.sep+"NSPipelineShelfSet.shelf"
    print(f"load shelves at path : {pipeline_shelf_path}")
    hou.shelves.loadFile(pipeline_shelf_path)
    hou.shelves.loadFile(pipeline_shelfSet)


def activate_shelf(shelf_name):
    """given the shelf name, access the current fesktop, add the shelf name to the shelf list and update it"""
    current_shelves_sets = [s for s in hou.ui.curDesktop().shelfDock().shelfSets()]
    shelf_set = current_shelves_sets[0]
    shelves = [s for s in shelf_set.shelves()]

    shelf_to_load = hou.shelves.shelves()[shelf_name]
    shelves.append(shelf_to_load)

    shelf_set.setShelves(shelves)
