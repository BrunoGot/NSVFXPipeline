import os
import pipeline_config as config
reload(config)

#create and manage pipeline folder structure according to the pipeline configuration file



def get_pipeline_datas_from_path(current_file_path):
    datas = {}
    # attribute from pipeline_configuration.py
    pipeline_base_folder = "03_WORK_PIPE"  # base folder name of the pipeline
    config = ["element", "asset_Type", "asset_name", "task", "subtask", "state"]
    pipeline_folder_depth = len(config)  # number of folder & subfolder to go to the file from the base folder

    pipeline_path = current_file_path.split(pipeline_base_folder)[1]
    pipeline_folders = pipeline_path.split("/")
    pipeline_folders.remove('')
    print("pipeline_folders = " + str(pipeline_folders))

    if(len(pipeline_folders)==pipeline_folder_depth):
        print("generating datas from path")
        for i in range(0,pipeline_folder_depth):
            datas[config[i]]=pipeline_folders[i]
    else:
        print("error")
    return datas

def create_new_work_version(current_file_path):
    # attribute from pipeline_configuration.py
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