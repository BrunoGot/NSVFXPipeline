import hou
import pipeline.fileSystem as fs
reload(fs)

def run():
    new_path = fs.create_new_work_version(hou.hipFile.path())
    hou.hipFile.save(new_path)
    return new_path