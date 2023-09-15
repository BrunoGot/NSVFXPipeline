import sys
import os
lucidity_path = r"C:\Users\Natspir\AppData\Local\Programs\Python\Python39\Lib\site-packages"

if lucidity_path not in sys.path:
    sys.path.append(lucidity_path)
import lucidity

import importlib
path = r"D:\Documents\Code\Python\NSVFXPipeline\pipeline"
if path not in sys.path :
    sys.path.append(path)
import pipeline_config as config

#from pipeline.tools.GUI import modal_messages as msg

#create and manage pipeline folder structure according to the pipeline configuration file

conf = config.Config("default") #make a singleton or something but there it smell like ten spirit

asset_base_path = conf.project_directory.pattern # r'C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D' #todo : set a getter or propriaty name home_project_path refering to the invariable root path
print("asset_base_path = "+asset_base_path)

def get_pipeline_datas_from_path(current_file_path):
    datas = {}
    # attribute from pipeline_configuration.py
    pipeline_base_folder = "03_WORK_PIPE"  # base folder name of the pipeline
    config = ["element", "asset_Type", "asset_name", "task", "subtask", "state"]
    pipeline_folder_depth = len(config)  # number of folder & subfolder to go to the file from the base folder

    pipeline_path = current_file_path.split(pipeline_base_folder)[1]
    pipeline_folders = pipeline_path.split("/")
    pipeline_folders.remove('')
    #smel : temporary
    if('3d' in pipeline_folders ):
        pipeline_folders.remove('3d')
    if('scenes' in pipeline_folders ):
        pipeline_folders.remove('scenes')

    print("pipeline_folders = " + str(pipeline_folders))

    if(len(pipeline_folders)==pipeline_folder_depth):
        print("generating datas from path")
        for i in range(0,pipeline_folder_depth):
            datas[config[i]]=pipeline_folders[i]
    else:
        print("error")
    return datas

def create_new_work_version(current_file_path):
    #xreate a new work version and get datas from the path
    # attribute from pipeline_configuration.py
    #conf = config.Config("default")
    #conf.asset_file_path.format()
    work_folder_template = "work_v"
    file_name_template = config.file_name_template
    print("path = "+current_file_path)
    path = os.path.dirname(current_file_path)
    file_extenction = os.path.basename(current_file_path).split('.')[-1]
    datas = get_pipeline_datas_from_path(path)

    #count number of work folder
    work_folder = current_file_path.split(datas["state"])[0]
    print("work_folder = "+str(work_folder))
    index = 1
    for work in os.listdir(work_folder):
        if(work_folder_template in work):
            print(work)
            index+=1

    new_work = work_folder_template+"{:03d}".format(index)
    print("new_work = "+new_work)
    new_path = os.path.join(str(work_folder),new_work)
    print("file_extenction = "+file_extenction)
    new_file_name = file_name_template.format(datas["asset_name"], index)
    new_file_name+="."+file_extenction
    os.mkdir(new_path)
    new_path = os.path.join(new_path,new_file_name)
    print("new_path = "+new_path)
    return new_path

def create_publish_folder(current_file_path):
    #templates
    publish_folder = "publish"
    publish_name_template = "{}_pulished"

    path = os.path.dirname(current_file_path)
    file_extenction = os.path.basename(current_file_path).split('.')[-1]
    datas = get_pipeline_datas_from_path(path)

    new_file_name = publish_name_template.format(datas["asset_name"])
    new_file_name+="."+file_extenction

    publish_path = path.split(datas["state"])[0]
    publish_path = os.path.join(publish_path,publish_folder)
    if os.path.exists(publish_path)==False:
        os.mkdir(publish_path)

    publish_path = os.path.join(publish_path,new_file_name)
    print("publish_path = "+publish_path)
    return publish_path

def create_new_task(file_path, task_name, subtask_name):
    print("file_path")
    #get datas from file_path, create new folder task from the user inputs
    path = os.path.dirname(file_path)

    datas = get_pipeline_datas_from_path(path)

    file_extenction = os.path.basename(file_path).split('.')[-1]
    new_file_name = config.file_name_template.format(datas["asset_name"], 1)
    new_file_name += "." + file_extenction

    task_path = file_path.split(datas["task"])[0]
    task_path+=task_name
    print("task_path = "+task_path)
    if(os.path.exists(task_path)):
        print("handle task already exist situation")
    else:
        task_path = os.path.join(task_path,subtask_name)
        print("pipeline = "+config.work_folder_template)
        task_path = os.path.join(task_path, config.work_folder_template.format(1))
        os.makedirs(task_path)
    task_path = os.path.join(task_path, new_file_name)
    return task_path

def get_folder_path(datas):
    """return the path according to the input data and the configuration file. this function may be temporary.
    Datas are a dictionnary with AssetType, AssetName, Task, Subtask, Version"""
    conf = config.Config("default")
    #cleaning the datas before format the path to avoid keyword duplication like "work_work_001"#
    raw_pattern = conf.version.pattern
    for k in conf.version.keys():
        raw_pattern = raw_pattern.replace("{"+k+"}","")
    if raw_pattern in datas['Version']:
        pass
        datas['Version'] = datas['Version'].replace(raw_pattern, "")
    ##
    try:
        path = conf.asset_file_folder_path.format(datas)
    except lucidity.error.FormatError as err:
        msg.error("The config name is invalid to save", str(err.args))
    return path

def get_datas_from_path(path):
    """parsing assets datas from the pipeline path. return the parsed datas using lucidity. May be temporary function"""
    conf = config.Config("default")
    try:
        asset_path = _isolate_asset_path(path)
        datas = conf.asset_file_path.parse(asset_path)
    except lucidity.ParseError as e:
        print(f"error reading path : {e}")
        datas = None
    return datas


def get_cache_folder(datas):
    """
    return the path to the cache folder according to the input datas
    :param datas:  {'AssetName': 'SessionBulleATruc', 'AssetType': 'MotionDesign', 'Subtask': 'HoudiniBFull', 'Task': 'HexagonParticles', 'Version': '001', 'ext': 'hipnc'}

    :return:
    """
    cache_path = conf.caches_path.format(datas)
    cache_path = os.path.join(asset_base_path,cache_path)
    return cache_path


def _isolate_asset_path(path):
    """
    get a file path from the saved scene and isolate the pipeline asset path
    :return str asset_path:
    """
    print("path = {}".format(path))
    asset_path = path.replace("\\", "/")
    print("asset_base_path = {}".format(asset_base_path))
    if asset_base_path in asset_path:
        asset_path = asset_path.replace(asset_base_path + "/", "")
    print("isolated path = {}".format(asset_path))
    return asset_path

def get_render_path(path):
    conf = config.Config("default")
    asset_path = _isolate_asset_path(path)
    datas = conf.asset_file_path.parse(asset_path)
    return conf.render_path.format(datas)

def get_publish_path(path):
    conf = config.Config("default")
    asset_path = _isolate_asset_path(path)
    datas = conf.asset_file_path.parse(asset_path)
    # print(datas)
    return conf.publish_path.format(datas)


def increment(path_file):
    #get the datas from the path
    datas = get_datas_from_path(path_file)
    print("datas = "+str(datas))
    #if datas are valids :
    if datas :
        digit_version = datas["Version"]
        folder_name = conf.version.format({"Version":digit_version})
        exist = True
        new_path = path_file
        while exist == True:
            #convert to in, increment it, then convert it back to string
            print("digit_version = "+digit_version)
            try:
                digit_version = int(digit_version)
            except ValueError as err:
                msg.error("probleme with version name template", "cannot convert this name into int : "+digit_version)
                print("err")
                break
            digit_version+=1
            digit_version = f"{digit_version:03}"
            #update the datas with the new work iteration
            datas["Version"] = digit_version
            new_path = get_folder_path(datas)
            new_path = os.path.join(new_path, conf.asset_file_name.format(datas))
            new_path = asset_base_path+"/"+new_path #os.path.join(asset_base_path,new_path)
            #print("new_path = "+new_path)
            #if the path doesn't exist yet, it's ok let's break the loop, else go for a new iteration
            if not os.path.exists(new_path):
                print("break the loop ")
                folder_path = os.path.join(asset_base_path, get_folder_path(datas))
                if not os.path.exists(folder_path) :
                    os.makedirs(folder_path)
                exist = False
        print("new_path = "+new_path)
    else :
        print("no datas")
        msg.error("problems with datas",datas)
if __name__ == "__main__":
    pass