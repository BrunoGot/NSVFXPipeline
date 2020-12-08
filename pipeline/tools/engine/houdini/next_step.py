import publish
import pipeline.fileSystem as fs
import hou
import os

reload(fs)
reload(publish)

def next(next_step_name, next_substep_name):
    datas = fs.get_pipeline_datas_from_path(os.path.dirname( hou.hipFile.path()))
    print("datas = "+str(datas))
    out_caches = publish.run()
    #here save in a buffer the cache path in the published file
    out_caches_path = []
    for cache in out_caches:
        out_caches_path.append(cache.parm("file").eval()) #problem it override the $F symbole

    new_path = fs.create_new_task(hou.hipFile.path(), next_step_name, next_substep_name)
    hou.hipFile.save(new_path)
    root_node = hou.node("/obj").createNode("geo", datas["task"])
    root_node.setDisplayFlag(False)
    for i in range(0,len(out_caches)):
        cache = out_caches[i]
        cache_path = out_caches_path[i]
        node_name = cache.name().replace("_out", "_in")
        in_node = root_node.createNode("NS_In",node_name)
        in_node.parm("file").set(cache_path) #link here the published caches
        geo_parent = cache.parent()
        geo_parent.deleteItems(geo_parent.allItems()) #reset the node
        #import th published cache inside it
        obj_merge = geo_parent.createNode("object_merge",node_name )
        obj_merge.parm("objpath1").set(in_node.path())
        obj_merge.setDisplayFlag(True)
    #preapre the scene for the new task
    hou.hipFile.save(new_path)

