
def explore():
    import hou
    import subprocess
    import os
    path = os.path.dirname(hou.hipFile.path())
    path = path.replace('/',os.sep)
    print("os.sep = "+os.sep)
    cmd = r'explorer /select,"'+path+'"'
    #cmd = r'explorer /select,"C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D/MotionDesign/ParticleAdvection_2LookDev/LookDev/work_v001"'

    #subprocess.Popen(r'explorer /select,"C:\Users\Natspir\Videos\VJing\DXV\Prod"')
    print(cmd)
    subprocess.Popen(cmd)

import hou
import subprocess
import os
path = os.path.dirname(hou.hipFile.path())
path = path.replace('/', os.sep)
print("os.sep = " + os.sep)
cmd = r'explorer /select,"' + path + '"'
# cmd = r'explorer /select,"C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D/MotionDesign/ParticleAdvection_2LookDev/LookDev/work_v001"'

# subprocess.Popen(r'explorer /select,"C:\Users\Natspir\Videos\VJing\DXV\Prod"')
print(cmd)
subprocess.Popen(cmd)
print("explore works")