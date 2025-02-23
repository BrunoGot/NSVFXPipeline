import sys
import os
import hou
#from pipeline import framework_config as framework
#file executed by houdini when starting
#just add the path to this file in the en var HOUDINI_SCRIPT_PATH

print("load NSpipeline : "+os.getcwd())
pipeline_path = r"D:\Documents\Code\Python\NSVFXPipeline" #framework.get_framework_path()

if(pipeline_path not in sys.path):
    sys.path.append(pipeline_path)

import pipeline.framework_config as frameworkConfig
houdini_tools_path = r"D:\Documents\Code\Python\NSVFXPipeline\pipeline\tools\engine" #os.path.join(pipeline_path,frameworkConfig.get_framework_path())
print("houdini_tools_path = "+houdini_tools_path)
if(houdini_tools_path not in sys.path):
    print("add path to houdini tools in sypath")
    sys.path.append(houdini_tools_path)

from houdini import shelf_manager #.shelf_manager as shelves

#houdini configuration
#maybe separate this code in an other py file
print("set environement variables.....")
#hou.putenv("HOUDINI_GEOMETRY_PATH", hou.hipfile.path()+"cache")
dirpath = os.path.dirname(hou.hipFile.path())
hou.hscript("set -g HOUDINI_GEOMETRY_PATH = " +"\$HIP/cache")
#use load_shelves() => hou.hscript("set -g HOUDINI_TOOLBAR_PATH = " +r'"C:/Users/Natspir/Documents/houdini18.0/toolbar/custom";&')
print("HOUDINI_GEOMETRY_PATH = "+ "$HIP/cache")
#print("HOUDINI_TOOLBAR_PATH = "+ hou.getenv("HOUDINI_TOOLBAR_PATH"))

#set shelves :
shelf_manager.load_shelf()

#import HDAs
hda_folder = frameworkConfig.get_HDAs_folder()
for hda in os.listdir(hda_folder):
    print("HDA loaded = "+hda)
    hda_path = hda_folder+os.sep+hda
    hou.hda.installFile(hda_path)
"""small exemple about how to add callback event    
print("colors settings")
hou.hscript("colorsettings -p -A")
def scene_event_callback(event_type):
    print("event_type = {}".format(event_type))
    if event_type == hou.hipFileEventType.AfterLoad:
        r = hou.hscript("colorsettings -p -A")
        print(r)
hou.hipFile.addEventCallback(scene_event_callback)

"""
#for all elements in HDA folder
#   instal HDAs