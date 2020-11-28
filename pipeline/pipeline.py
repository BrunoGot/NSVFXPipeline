import sys
import os

pip_path = os.path.dirname(__file__)

if pip_path not in sys.path:
    sys.path.append(pip_path)

