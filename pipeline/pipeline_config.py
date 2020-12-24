#file structure organisation and enironement path
#todo: parse a json file
cache_path = "$HIP/cache"
render_path = "$HIP/render"
flip_path = "$HIP/flip"

work_folder_template = "work_v{:03d}"
file_name_template = "{}_v{:03d}"
out_img_patern = "$hipname.mantra_ipr.$F.exr"

__pipeline_path = r"C:\Users\Natspir\Prod\projects"

def get_pipeline_path():
    return __pipeline_path

def get_cache_path():
    return cache_path

def get_render_path():
    return render_path

def get_flip_path():
    return flip_path

def get_out_img_patern():
    return out_img_patern