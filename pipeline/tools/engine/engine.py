import os
import pipeline.fileSystem as fs
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
