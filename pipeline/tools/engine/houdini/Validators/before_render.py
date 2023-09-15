import hou

def check_zombies_parameters():
    """called by the shelf tool, to check for any parameters or object that doesn't exist in the scene anymore,
    "the zombies" """

    mantra_zombies = check_mantra_object_exist()
    wedges_zombies = check_wedge_param_linked()
    print(f"wedges_zombies = {wedges_zombies}")
    errors = mantra_zombies+wedges_zombies
    if len(errors) < 1:
        hou.ui.displayMessage("All Good !")
    else:
        hou.ui.displayMessage("\n".join(errors))

def check_mantra_object_exist():
    """
    Check if the object refered in candidate object of the mantra node exist
    :return:
    """
    node_type = hou.nodeType(hou.ropNodeTypeCategory(),"ifd")
    all_node = node_type.instances()
    errors = []
    for n in all_node:
        obj = n.parm("vobject").eval()
        if obj == "" or obj != "*" and hou.node(f"/obj/{obj}") is None:
            errors.append(f"{n.path()} has a broken object link : {obj}")
    return errors

def check_wedge_param_linked():
    """
    check if the wedgers refer to a linked node
    todo:check if it's refer to a linked parameter
    :return:
    """
    errors = []
    node_type = hou.nodeType(hou.ropNodeTypeCategory(), "wedge")
    all_node = node_type.instances()
    print(f"all_nodes = {all_node}")
    for n in all_node: #for all wedges
        #check number of wedges
        nb_wedges = n.parm("wedgeattributes")
        print(f"nb_wedge  {nb_wedges}")
        for i in range(0,nb_wedges):
            #check if wedge param is ON
            channel_id = i+1
            if n.parm(f"exportchannel{channel_id}").eval() == 1:
                #check if wedge param is linked
                obj = n.parm(f"channel{channel_id}")
                if not hou.node(obj):
                    errors.append(f"{n.path()} has a broken object link : {obj}")
    return errors