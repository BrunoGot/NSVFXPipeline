from multiprocessing import Process, Queue, Pipe
import sys
path = r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline'
if path not in sys.path:
    sys.path.append(path)

from pipeline.tools.GUI import save_asset_gui
import subprocess
import os
from multiprocessing import Pool

if __name__ == "__main__":
    subprocess.call([r'C:\Users\Natspir\Documents\Code\Python\AssetManager\venv\Scripts\Python.exe',
                      r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\GUI\save_asset_gui.py'])

