import os
from pathlib import Path

from krita import *

from pipeline.tools.engine import engine
from pipeline import fileSystem as fs

def save(datas):
    asset_datas = datas  # engine.save_asset(path) #save_asset() should be named other like get asset_datas
    ###todo:should go into a new save_asset method from engine###
    if asset_datas:
        if "ext" not in asset_datas:
            asset_datas["ext"] = "kra"
        base_path = engine.make_asset_path(asset_datas)
        path_id = os.path.join(base_path, fs.conf.asset_file_name.format(asset_datas))
        print("path_id = {}".format(path_id))
    print("path ready to save = {}".format(path_id))
    ###
    if path_id:
        base_path = base_path.replace("\\", "/")
        print("JOB1 = {}".format(base_path))
        os.environ["JOB"] = base_path
        #use krita api
        doc = Krita.instance().activeDocument()
        if os.path.exists(doc.fileName()):  # si le fichier a déja été sauvegardé une fois
            doc.setFileName(path_id)
            doc.save()
        else:
            doc.saveAs(path_id)
    return path_id

def export_image(type="png"):
    """
    used by ns_pipeline.py for Krita in %appdata%/krita/pyktita
    :param type:
    :return:
    """

    #will have to go in a pref file
    export_options = {
        "compression": 9,
        "quality": 100
    }
    document = Krita.instance().activeDocument()
    if document:
        path = document.fileName()
        if path:
            #set path and file format
            # out_folder_path = fs.get_publish_path(path)
            out_folder_path = fs.asset_base_path / Path(fs.get_publish_path(path))
            if not os.path.exists(str(out_folder_path)):
                os.makedirs(str(out_folder_path), exist_ok=True)
            base_name = os.path.basename(path) #.replace('.kra','.png')
            # out_path = os.path.join(out_folder_path,base_name)

            out_path = out_folder_path / base_name
            out_path = out_path.with_suffix('.png')
            out_path = out_path.as_posix()

            #export
            info_obj = krita.InfoObject()
            info_obj.setProperties(export_options)
            document.exportImage(out_path,info_obj)