import hou

def get_all_displayed_nodes():
    display_nodes = []
    geo_nodes = hou.node("/obj").children()
    print("update")
    for geo in geo_nodes:
        if geo.isDisplayFlagSet()==1:
            for node in geo.children():
                if(node.isDisplayFlagSet()==1):
                    print(node.name())
                    display_nodes.append(node)
    return display_nodes

def caching_nodes(nodes):
    """check all nodes of the list.
    If it's caches, do nothing,
    else add a cache node and bake the result"""

    for node in nodes:
        if(node.parm("file")):
            print("cache detected : move it to the publish folder ?")
        else:
            cache = node.createOutputNode("filecache",node.parent().name()+"_"+node.name()+"_out")
            cache.setDisplayFlag(True)

def run():
    nodes = get_all_displayed_nodes()
    caching_nodes(nodes)