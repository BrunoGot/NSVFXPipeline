import os
import importlib
import hou

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs
importlib.reload(engine)
importlib.reload(fs)

def save(datas):
    path_id = hou.hipFile.path()
    asset_datas = datas  # engine.save_asset(path) #save_asset() should be named other like get asset_datas
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
        #prepare env vars
        global_vars = {}
        global_vars["JOB"] = houdinize_path(base_path)
        cache_path =  fs.get_cache_folder(asset_datas)
        global_vars["CACHE"] =houdinize_path(cache_path)
        for k,v in asset_datas.items():
            global_vars[k.upper()] = v
        set_houdini_variables(global_vars)

        hou.hipFile.save(path_id)
    return path_id


def houdinize_path(path):
    """turn \\ to / in a path to make it compatible with houdini"""
    return path.replace("\\","/")


def set_houdini_variables(dic_values):
    """
    Set Houdini env var according to the dictionary
    :param dic_values: {var_name : var_alue}
    """
    for k, v in dic_values.items():
        os.environ[k] = v
        hou.hscript(f"set -g {k} = {v}")  # -g makes the variable global
        print(f"env var set {k} : {v}")
