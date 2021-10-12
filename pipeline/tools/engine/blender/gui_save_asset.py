import sys
from Qt import QtWidgets
from pipeline.tools.engine import engine

def save_asset(path):
    #path = r"C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D\\Save_as\\Pipeline_Test\\Blender\\Deployment_Test\\001\\MandalaPower_007.blend"
    """print("test")
    import subprocess
    path_file = path
    p = subprocess.Popen([r'C:\\Users\\Natspir\\Documents\\Code\\Python\\AssetManager\\venv\\Scripts\\Python.exe',
                          r'C:\\Users\\Natspir\\Documents\\Code\\Python\\NSVFXPipeline\\pipeline\\tools\\GUI\\save_asset_gui.py',
                          '--path=' + path_file, '--ext=kra'], shell=True, stdout=subprocess.PIPE)
    return p"""
    return engine.save_asset(path, "blend")

if __name__ == "__main__":
    p = save_asset(r"C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D\\Save_as\\Pipeline_Test\\Blender\\Deployment_Test\\001\\MandalaPower_007.blend")
    print("p = "+p)