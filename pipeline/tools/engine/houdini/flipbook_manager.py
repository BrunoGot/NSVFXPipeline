import os
import hou
import pipeline.pipeline_config as config
reload(config)

def view_render():
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