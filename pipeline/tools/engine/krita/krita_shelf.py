import os
import subprocess
import sys

lib_path_pipeline = r"D:\Documents\Code\Python\NSVFXPipeline\pipeline"

if lib_path_pipeline not in sys.path:
    sys.path.append(lib_path_pipeline)

from pipeline.tools.engine.krita import krita_engine
from pipeline import fileSystem as fs
from pipeline.tools.engine.krita.krita_save_ui import KritaSaveUI

import sys
import importlib
importlib.reload(krita_engine)

###############


#################
tool = None
def save_asset(path_file, mainWindow):
    return KritaSaveUI(krita_engine, path_file)#SaveConceptGUI(mainWindow)

def export():
    krita_engine.export_image()

def cleaning(out_bstring):
    out = str(out_bstring)
    out = out.split("=")
    out = out[1]
    out = out.replace(r"\r\n'", "")
    out = out.replace(" ", "")
    return out

def increment(path_file):
    p = subprocess.Popen([r'C:\Users\Natspir\Documents\Code\Python\AssetManager\venv\Scripts\Python.exe',
                          r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\engine\increment.py',
                          '--path=' + path_file], shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    new_path = ""
    err = p.stderr.readlines()
    if len(err)>=1:
        print("errors : "+str(err))
        new_path = str(p.stderr.readlines())
    else:
        out = p.stdout.readlines()
        for i in out:
            print(i)
            if b'new_path =' in i:
                new_path = i
                new_path = cleaning(new_path)
                print("path found, new_path = "+new_path)

    return new_path

        #print("digit = "+digit)

    #   increment work folder
    #   remake new_path
    #   return new_path

if __name__=="__main__":
    save_asset("D:/NatspirProd/03_WORK_PIPE/01_ASSET_3D/Concept/MandalaPower/Psyched/Base/007/MandalaPower_007.kra")
    #increment("C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D/Concept/MandalaPower/Psyched/Base/007/MandalaPower_007.kra")
    """import subprocess
    path_file = r"D:\\NatspirProd\\03_WORK_PIPE\\01_ASSET_3D\\Concept\\MandalaPower\\Psyched\\Base\\006\\MandalaPower_006.kra"
    p = subprocess.Popen([r'C:\\Users\\Natspir\\Documents\\Code\\Python\\AssetManager\\venv\\Scripts\\Python.exe',
                              r'C:\\Users\\Natspir\\Documents\\Code\\Python\\NSVFXPipeline\\pipeline\\tools\\GUI\\save_asset_gui.py',
                              '--path='+path_file, '--ext=kra'], shell=True, stdout=subprocess.PIPE)"""