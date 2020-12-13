#here are stored the file path of all lmodule of the framework. Update this file if there is some changes in the structure of the framework
#todo : divide it in two part. one json file containing strings and file path, and the .py file reading this doc and returning value to the rest of the code

houdini_tools_path = r"pipeline\tools\engine"
#todo : create a new env var VFX_PIPELINE that pointing on the pipeline base folder
__pipeline_path = r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline"

def get_houdini_path():
    return houdini_tools_path

def get_pipeline_path():
    return __pipeline_path