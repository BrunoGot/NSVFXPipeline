import os
import pipeline.fileSystem as fs
import importlib
import subprocess

importlib.reload(fs)
"""common framework for all engine"""
def make_asset_path(asset_datas):
    #asset_datas is a pack of infos as {"AssetType" : asset_type,"AssetName" : asset_name, "Task" : task, "Subtask" : subtask, "Version" : version}

    #base root path of the project
    project_path = fs.asset_base_path
    print("project path = "+project_path)

    #generate the path from theses datas
    path = os.path.join(project_path, fs.get_folder_path(asset_datas))
    path.replace("\\","/")
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

def save_asset(path_file="", ext=""):
    print("check if datas can be extrcated from the input path")
    datas = None
    if path_file:
        datas = fs.get_datas_from_path(path_file)
        print("datas = {}".format(datas))
    if datas:
        p = subprocess.Popen(
            [r"D:\Documents\Code\C++\NSPipelineGUI\NSPipelinePOC\Builds\VisualStudio2022\x64\Debug\App\NSPipelinePOC.exe",
             datas["AssetType"], datas["AssetName"],datas["Task"],datas["Subtask"],datas["Version"]], shell=False,
            stdout=subprocess.PIPE)
    else :
        p = subprocess.Popen(
            [r"D:\Documents\Code\C++\NSPipelineGUI\NSPipelinePOC\Builds\VisualStudio2022\x64\Debug\App\NSPipelinePOC.exe"], shell=False,
            stdout=subprocess.PIPE)

    print("test")
    print("### out process ###")
    asset_datas = {}
    raw_datas = ""
    for i in p.stdout.readlines():
        print(i)
        if b"out path = " in i:
            raw_datas = str(i)
            raw_datas = raw_datas.replace("out path = ", "")
            raw_datas = raw_datas.replace(" ", "")
            raw_datas = raw_datas.replace("b'", "")
            raw_datas = raw_datas.replace(r"\r\n'", "")
            break
    if raw_datas:
        raw_datas = raw_datas.replace(" ", "")
        for d in raw_datas.split(","):
            # cleaning out string :
            data = d.split(":")
            asset_datas[data[0]] = data[1]
    print("result = {}".format(asset_datas))
    print("### end out processs ###")

    return asset_datas

if __name__=="__main__":
    save_asset(path_file="D:/Prod/03_WORK_PIPE/01_ASSET_3D/Tutorial/PopNetTextureTrail/HDACreation/1/v002/PopNetTextureTrail_v002.hipnc")