import os
import pipeline.fileSystem as fs
import importlib
importlib.reload(fs)
"""common framework for all engine"""
def make_asset_path(asset_datas):
    #asset_datas is a pack of infos as {"AssetType" : asset_type,"AssetName" : asset_name, "Task" : task, "Subtask" : subtask, "Version" : version}

    #base root path of the project
    project_path = fs.asset_base_path
    print("project_path = "+project_path)

    #generate the path from theses datas
    path = os.path.join(project_path, fs.get_folder_path(asset_datas))

    #make the path
    #if the path doesn't exist create it
    if not os.path.exists(path):
        os.makedirs(path)
    #else:
        #display a warning message and ask for overight
    print(path)
    return path

def explore_file(path):
    print("open path")
    os.startfile(path)

def save_asset(path_file, ext):
    import subprocess
    p = subprocess.Popen([r'D:\Documents\Code\Python\AssetManager\venv\Scripts\Python.exe',
                          r'D:\Documents\Code\Python\NSVFXPipeline\pipeline\tools\GUI\save_asset_gui.py',
                          '--path='+path_file, '--ext='+ext], shell=True, stdout=subprocess.PIPE)
    print("test5")
    out = ""
    print("### out process ###")
    #print(p.stdout.readlines())
    print("### end out processs ###")
    for i in p.stdout.readlines():
        print(i)
        if b"save path_id" in i:
            out = str(i)
            #cleaning out string :
            out = out.split("=")
            out = out[1]
            out = out.replace(r"\r\n'", "")
            out = out.replace(" ","")
    print("out = "+out)
    return out