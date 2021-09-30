import sys
path = r"C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline"
if path not in sys.path :
    sys.path.append(path)

import framework_config
import os
#file structure organisation and enironement path

#todo : define a houdini config path to handle default template and env var relative to houdini soft
#todo: parse a json file

######## obselete ##########
cache_path = "$HIP/cache"
render_path = "$HIP/render"
flip_path = "flip"

work_folder_template = "work_v{:03d}"
file_name_template = "{}_v{:03d}"
out_img_patern = "$hipname.mantra_ipr.$F4.exr"
out_flip_pattern = ".flip.$F4.jpeg"

__pipeline_path = r"C:\Users\Natspir\Prod\projects"

def get_pipeline_path():
    return __pipeline_path

def get_cache_path():
    return cache_path

def get_render_path():
    return render_path

def get_flip_path():
    return flip_path

def get_flip_pattern():
    return out_flip_pattern

def get_out_img_patern():
    return out_img_patern
#####################################

"""This script load config file and parse it to return location of the different folder of the VFX pipeline => Config.render_path"""
import yaml
import lucidity

class Config():

    @property
    def asset_path(self):
        return self.__templates["AssetPath"]

    @property
    def project_directory(self):
        return self.__templates["Project"]

    @property
    def asset_file_path(self):
        return self.__templates["AssetFilePath"]

    @property
    def asset_file_folder_path(self):
        return self.__templates["FileFolder"]

    @property
    def asset_file_name(self):
        return self.__templates["AssetFileName"]

    @property
    def workspace_path(self):
        return self.__templates["Workspace"]

    @property
    def caches_path(self):
        return self.__templates["Caches"]

    @property
    def render_path(self):
        return self.__templates["Render"]

    @property
    def flip_path(self):
        return self.__templates["Flip"]

    @property
    def textures_path(self):
        return self.__templates["Textures"]

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__templates["Version"]

    def __init__(self, name, config_path = "config.yml"):
        self.key_value = ["$Project", "$AssetFileName", "$AssetPath", "$FileFolder", "$Workspace", "$Caches", "$Render", "$Flip", "$Textures",
                          "$Version"]
        #dictionary of lucidity template
        self.__name = name
        self.__templates = self.parsing_config_file(config_path)

    def parsing_config_file(self, config_file):
        """parse the yaml file and return some lucidity patterns """
        path = framework_config.get_framework_path()+os.sep+"pipeline"+os.sep+config_file
        #print("path = "+path)
        templates = {}
        #parsing the config yml file
        yaml_file = open(path, 'r')
        yaml_content = yaml.safe_load(yaml_file)

        #print("key : value")
        for key, value in yaml_content.items():
            #print(f"Key value = {key}: {value}")
            raw_value = value
            for i in range(0,value.count('$')): #loop over all keywork begining with $
                #print("dolar word = "+str(i))
                for key_word in self.key_value:  # determine wich key is it
                    if key_word in value: #if the detected key has been found
                        #print("detected key_word = " + key_word)
                        detected_key = key_word.replace("$", '')  # delete the "$" symbol
                        raw_value = raw_value.replace(key_word, yaml_content[detected_key])
                        #print("raw_value = "+raw_value)
                        yaml_content[key] = raw_value#value.replace(key_word, yaml_content[detected_key])  # assign the new value

            """if("$" in value): #detect a keyvalue in the string
                for i in self.key_value: #determine wich key is it
                    if i in value: #if the detected key has been found
                        print("detect i = "+i)
                        detected_key = i.replace("$", '') #delete the "$" symbol
                        print("yaml_content[key] = "+yaml_content[key])
                        yaml_content[key] = value.replace(i,yaml_content[detected_key] ) #assign the new value
                        print("yaml_content[key]2 = "+yaml_content[key])
                        #print("new value = "+yaml_content[key])"""
            templates[key] = lucidity.Template(key, yaml_content[key])
        return templates

    """def list_templates(self):
        print("##list templates : ")
        for key, value in self.__templates.items():
            print(f"{key}: {value.pattern}")"""
    #test lucidity
    """template_file = lucidity.Template('file', yaml_content["File"])
    template_workspace = lucidity.Template('workspace', yaml_content["Workspace"])
    template_render = lucidity.Template('render', yaml_content["Render"])
    print(template_file.pattern)
    print(template_workspace.pattern)
    print(template_render.pattern)"""
