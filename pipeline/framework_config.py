import os
#here are stored the file path of all lmodule of the framework. Update this file if there is some changes in the structure of the framework
#todo : divide it in two part. one json file containing strings and file path, and the .py file reading this doc and returning value to the rest of the code

houdini_tools_path = r"pipeline\tools\engine"
#todo : create a new env var VFX_PIPELINE that pointing on the pipeline base folder
__framework_path = r"D:\Documents\Code\Python\NSVFXPipeline"
HDA_folder = __framework_path+os.sep+houdini_tools_path+os.sep+r"houdini\HDAs"

def get_houdini_path():
    return houdini_tools_path

def get_framework_path():
    return __framework_path

def get_HDAs_folder():
    return HDA_folder
#def