import importlib

import hou

from pipeline.tools.engine.houdini import save_as_asset

importlib.reload(save_as_asset)

def run():
    """
    Save a new version but still load on the current version
    :return:
    """
    cur_path = hou.hipFile.path()
    path_version = save_as_asset.run()
    if path_version:
        print("version saved as {}".format(path_version))
        hou.hipFile.save(cur_path)
    else:
        print("No version saved")
