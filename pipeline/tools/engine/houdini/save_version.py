import hou
import pipeline.fileSystem as fs
reload(fs)

def run():
    cur_path = hou.hipFile.path()
    #file = pipeline_file(cur_path)  # parse the current pipeline file to get some informations
    new_path = fs.create_new_work_version(cur_path)
    hou.hipFile.save(new_path)
    return new_path