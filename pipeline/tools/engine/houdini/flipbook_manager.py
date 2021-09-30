import os
import hou
import pipeline.pipeline_config as config
reload(config)

def view_render():
    """show in the mplay the last render"""

    render_path = config.get_render_path()
    hip = hou.hipFile.path()

    img_pattern = config.get_out_img_patern()
    filename = os.path.basename(hip)
    filename = filename.split(".hipnc")[0]
    img_pattern = img_pattern.replace("$hipname",filename )

    hip = os.path.dirname(hip)
    render_path = render_path.replace("$HIP",hip)
    file_found = False
    if os.path.exists(render_path) and len(os.listdir(render_path))>0:
        print("there is some render files")
        path = render_path
        file_found = True
    else:
        flip_path = config.get_flip_path()
        if os.path.exists(flip_path) and len(os.listdir(rendflip_pather_path))>0:
            path = flip_path
            file_found = True
        else:
            print("no file detected in flip or render folder")
            
    if file_found == True:
        os.system("mplay " + path + "/" + img_pattern)

    print(path)

def generate_flipbook():
    """generate a flip book from the current viewport"""
    import toolutils
    scene = toolutils.sceneViewer()
    flipbook_options = scene.flipbookSettings().stash()
    #flipbook_options.frameRange((0,20))

    #todo : define a houdini config path to handle default template and env var relative to houdini soft
    out_folder = os.path.dirname(hou.hipFile.path())+"/"+config.get_flip_path()
    filename = hou.hipFile.basename().replace(".hip","")
    out_path = out_folder+"/"+filename+config.get_flip_pattern()

    if( os.path.exists(out_folder)==False):#if the flip folder doesn't exist, create it
        os.makedirs(out_folder)
    print(out_path)
    flipbook_options.output(out_path)
    print(str(flipbook_options))
    scene.flipbook(settings=flipbook_options)