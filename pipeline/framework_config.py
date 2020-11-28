#here are stored the file path of all lmodule of the framework. Update this file if there is some changes in the structure of the framework
#todo : divide it in two part. one json file containing strings and file path, and the .py file reading this doc and returning value to the rest of the code

houdini_tools_path = r"pipline\tools\engine"

def get_houdini_path():
    return houdini_tools_path