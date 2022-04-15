import sys
import argparse

path = r'D:\Documents\Code\Python\NSVFXPipeline'
if path not in sys.path:
    sys.path.append(path)
import pipeline.fileSystem as fs

parser = argparse.ArgumentParser(description="Save asset")
parser.add_argument('--path', dest='path', type=str, help='path of the current asset to save')
args = parser.parse_args()
print("args = " + str(args.path))

if len(args.path)>1 :
    path = args.path#.replace("/",r"\\")
    print("arg = "+path)
    fs.increment(path)