import os
import subprocess

"""
r"\CreteParticles\AnimA\001\Hadra2023__CreteParticles__AnimA_001.blend",
         r"\MaskHashes\LightPlay\001\Hadra2023__MaskHashes__LightPlay_001.blend",
         r"\MaskHashes\Waves\002\Hadra2023__MaskHashes__Waves_002.blend",
         r"\OpenFace\AnimA\002\Hadra2023__OpenFace__AnimA_002.blend",
         r"\ShadertoyTexture\AnimA\001\Hadra2023__ShadertoyTexture__AnimA_001.blend",
         r"\Clouds\Shading_B\002\Hadra2023__Clouds__Shading_B_002.blend"
         r"\Clouds\Shading\002\Hadra2023__Clouds__Shading_002.blend"
         r"D:\Prod\03_WORK_PIPE\01_ASSET_3D\Chromatribe\Zurich_Christmas_2023\Petals\AllA_Shade\001\Zurich_Christmas_2023__Petals__AllA_Shade_001.blend"
"""

blender_exe = r"C:\Program Files\Blender Foundation\Blender 3.1\blender"
project = r"D:\Prod\03_WORK_PIPE\01_ASSET_3D\Chromatribe\Zurich_Christmas_2023"
files = [r"Petals\AllA_Shade\001\Zurich_Christmas_2023__Petals__AllA_Shade_001.blend",
         r"Petals\MiddleA_Shade\001\Zurich_Christmas_2023__Petals__MiddleA_Shade_001.blend"
         ]

files_to_render = []
#check if all files exists
for f in files:
    print(f"f = {f}")
    print(f"project = {project}")
    blend_file = os.path.join(project,f)
    if not os.path.isfile(blend_file):
        raise Exception(f"{blend_file} doesn't exist")
    print(f"{f} is ok to render")
    files_to_render.append(blend_file)
#Start renders
for f in  files_to_render:
    print(f"rendering {f}")
    subprocess.run([blender_exe, "-b",f , "-a"], shell=True)
    print(f"render {f} done")
print("all renders done")