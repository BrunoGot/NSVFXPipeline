import os
import hou
import pipeline
from pipeline import pipeline_config as config
reload(config)
project_path = config.get_pipeline_path()

def set_project(project_name):
    new_path = project_path+"\\"+project_name
    print("new path = "+new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    new_path = new_path.replace("\\","/")
    hou.hscript("set -g JOB = " + new_path)
        #hou.
    pass
    #create folder
    #set env var to the new path