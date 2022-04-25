import os
import importlib
import subprocess
import sys
import hou

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs
importlib.reload(engine)


def run():
    path_id = ""
    path = hou.hipFile.path()
    asset_datas = engine.save_asset(path) #save_asset() should be named other like get asset_datas
    ###todo:should go into a new save_asset method from engine###
    if asset_datas:
        if "ext" not in asset_datas:
            asset_datas["ext"] = "hipnc"
        base_path = engine.make_asset_path(asset_datas)
        path_id = os.path.join(base_path, fs.conf.asset_file_name.format(asset_datas))
        print("path_id = {}".format(path_id))
    print("path ready to save = {}".format(path_id))
    ###
    if path_id:
        print("base_path = {}".format(base_path))
        path_file = hou.hipFile.save(path_id)
        os.environ["JOB"] = base_path

if __name__ == "__main__":
    run()
