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
        base_path = base_path.replace("\\","/" )
        print("JOB1 = {}".format(base_path))
        os.environ["JOB"] = base_path
        hou.hscript("set -g JOB = {}".format(base_path))
        hou.hipFile.save(path_id)
    return path_id

if __name__ == "__main__":
    run()
