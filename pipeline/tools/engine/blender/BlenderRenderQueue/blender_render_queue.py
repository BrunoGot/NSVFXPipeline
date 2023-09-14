import os
import subprocess

"""
r"\CreteParticles\AnimA\001\Hadra2023__CreteParticles__AnimA_001.blend",
         r"\MaskHashes\LightPlay\001\Hadra2023__MaskHashes__LightPlay_001.blend",
         r"\MaskHashes\Waves\002\Hadra2023__MaskHashes__Waves_002.blend",
         r"\OpenFace\AnimA\002\Hadra2023__OpenFace__AnimA_002.blend",
         r"\ShadertoyTexture\AnimA\001\Hadra2023__ShadertoyTexture__AnimA_001.blend",
         r"\Clouds\Shading_B\002\Hadra2023__Clouds__Shading_B_002.blend"
"""

blender_exe = r"C:\Program Files\Blender Foundation\Blender 3.1\blender"
project = r"D:\Prod\03_WORK_PIPE\01_ASSET_3D\MotionDesign\Hadra2023"
files = [
         r"\Clouds\Shading\002\Hadra2023__Clouds__Shading_002.blend",]

#check if all files exists
for f in files:
    blend_file = project+f
    if not os.path.isfile(blend_file):
        raise Exception(f"{blend_file} doesn't exist")
    print(f"{f} is ok to render")
#Start renders
for f in  files:
    print(f"rendering {project+f}")
    subprocess.run([blender_exe, "-b",project+f , "-a"], shell=True)
    print(f"render {f} done")
print("all renders done")