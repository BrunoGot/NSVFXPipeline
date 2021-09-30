import hou
from pipeline import fileSystem as fs
from houdini import save_version as save_tool
reload(fs)

def get_all_displayed_nodes():
    display_nodes = []
    geo_nodes = hou.node("/obj").children()
    print("update")
    for geo in geo_nodes:
        if geo.isDisplayFlagSet()==1:
            display_nodes.append(geo.displayNode())
            print("out node = "+geo.displayNode().name())
            """for node in geo.children():
                print("node = "+node.name())
                if(node.isDisplayFlagSet()==1):
                    print(node.name())
                    display_nodes.append(node)"""

    return display_nodes

def caching_nodes(nodes):
    """check all nodes of the list.
    If it's caches, do nothing,
    else add a cache node and bake the result"""
    cache_node_type = "NS_Out" #pointing on a custom HDO. todo : create a config file mapping variable with custom HDA or default node to get like : HDATools.cache_node => returning "NS_OUT" or "filecache" if HDA exist or not

    caches = []
    for node in nodes:
        if(node.parm("file")):
            print("cache detected : move it to the publish folder ?")
            caches.append((node))
        else:
            cache = node.createOutputNode(cache_node_type,"out")
            cache.setName(node.parent().name() + "_" + node.name() + "_out",True)
            cache.setDisplayFlag(True)
            caches.append(cache)
    return caches

def baking_out_caches(caches):
    #todo: check if the cach have been already baked. If so, ask to do nothing or recalculate it. Also pull all caches that needed
    for cache in caches:
        print("baking cache "+cache.name())
        cache.parm("execute").pressButton()

def run():
    #save a version
    #create the out nodes
    #save the publish version in the publish folder
    #write the path of the work version somewere
    #baking/copying/moving all outcaches nodes
    nodes = get_all_displayed_nodes()
    save_tool.run()
    caches = caching_nodes(nodes)
    new_path = fs.create_publish_folder(hou.hipFile.path())
    hou.hipFile.save(new_path)
    baking_out_caches(caches)
    print("return caches = "+str(caches))
    return caches #return the list of out caches
