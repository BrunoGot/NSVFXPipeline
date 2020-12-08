import sys
import os
import hou
#file executed by houdini when starting
#just add the path to this file in the en var HOUDINI_SCRIPT_PATH

#todo : create a new env var VFX_PIPELINE that pointing on the pipeline base folder
pipeline_path = r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline"

print("load NSpipeline")

if(pipeline_path not in sys.path):
    sys.path.append(pipeline_path)

import pipeline.framework_config as frameworkConfig
houdini_tools_path = r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\engine" #os.path.join(pipeline_path,frameworkConfig.get_houdini_path())
print("houdini_tools_path = "+houdini_tools_path)
if(houdini_tools_path not in sys.path):
    print("add path to houdini tools in sypath")
    sys.path.append(houdini_tools_path)

#houdini configuration
#maybe separate this code in an other py file
print("set environement variables.....")
#hou.putenv("HOUDINI_GEOMETRY_PATH", hou.hipfile.path()+"cache")
dirpath = os.path.dirname(hou.hipFile.path())
hou.hscript("set -g HOUDINI_GEOMETRY_PATH = " +"\$HIP/cache")
print("HOUDINI_GEOMETRY_PATH = "+ "$HIP/cache")