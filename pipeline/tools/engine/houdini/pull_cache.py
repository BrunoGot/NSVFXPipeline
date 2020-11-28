import os
import re
import shutil
import hou

# pull the cache in the local directory
# ask if the cache must mbex move or just copied
print("code this script to move a cache localy")
"""
#####
get the list of all filecache
foreach():
    get the cache in the path 
    if exist :
        copy/move past this cache to the local destination
        update the cache path in the node
    else : 
        add in the node in the list of problem
        print the pb in a windows
        if the user want to fix it:
            print a windows to relocate the cache
"""


def listCaches():
    """list all the cache of a scene"""
    nodes = hou.node("/obj").allSubChildren()
    # print(hou.node("/obj/pyro_import/test"))
    listCache = []
    for n in nodes:
        if n.type().name() == "filecache":
            # print(n.name())
            listCache.append(n)
    return listCache


def pullFiles(srcDir, dstDir, fileNameTemplate, mode):
    sucess = True
    print("filename template = " + fileNameTemplate)
    print("copy/move past file from src to dst directory")
    """
    Todo : 
    get the fileNameTemplate, replace all the $F by '/d*' to make a regex expression
    filtre the good cache by using this regex 
    copy/move the filtered files
    """
    # remplace les symboles $F, $F4, $F10, $F100 par l'expression \d* pour filtrer tte mles different pass de frames
    filter = re.sub('\$F' + '\d*', '\d*', fileNameTemplate)
    # apply the filter on the input filename
    # print("filter = "+filter)

    for filename in os.listdir(srcDir):
        # filtering if the filename is matching with the filter USING REGEX
        if re.match(filter, filename):
            # if the dest not exist, create the dest path
            if not os.path.exists(dstDir):
                print("le chemin de dest n'existe pas : " + dstDir)
                os.mkdir(dstDir)
            # assemble the correct dest path and copy/move the files
            pathSrc = srcDir + os.sep + filename
            pathDst = dstDir + os.sep + filename
            if mode == 0:
                print("copy the file " + filename + " to the dst " + pathDst)
            elif mode == 1:
                print("move the file " + filename + " to the dst " + pathDst)
                shutil.move(pathSrc, pathDst)
            else:
                print("error")
    return sucess  # if no errors, return true

    # list all files in the src directory, and copy/move these matching name (regex ?)


####MAIN####
def run():
    houFile = hou.hipFile  # "C:\Users\Natspir\NatspirProd\03_WORK_PIPE\01_ASSET_3D\MotionDesign\ParticleAdvection_2LookDev\LookDev\work_v001"
    basePath = os.path.dirname(houFile.path())
    print("pull all the caches of a scene")
    caches = listCaches()
    if( len(caches)>0):
        for cache in caches:
            """For each cache, detect if it's already in the good location or not. 
            If not, trig a msg to ask if the user want to copy or move the cache in the good directory"""
            # get the raw value of the file path to keep the $F symbole
            rawPath = cache.parm("file").rawValue()
            if "chs(" in rawPath:
                # print('hou.evalParm(cache.parm("file")) = '+hou.evalParm(cache.parm("file")))
                cache = cache.parm("file").getReferencedParm().node()  # relocate the referenced node
                rawPath = cache.parm("file").rawValue()  # get the raw value of the referenced node
            rawPath = rawPath.replace("$HIPNAME", hou.hipFile.name())
            rawPath = rawPath.replace("$OS", cache.name())
            print("cache.name() = " + cache.name())
            fileName = os.path.basename(rawPath)
            print(" rawPath = " + rawPath)

            path = cache.parm("file").eval()
            # define the dir path
            '''tabDir = path.split("/")
            nbSep = len(tabDir)
            fileName = tabDir[nbSep-1]
            dirPath = path.replace(fileName, "")'''
            srcPath = os.path.dirname(path)
            destPath = basePath + os.sep + "caches" + os.sep + cache.name()
            print(destPath)
            if srcPath != destPath:
                # display the message
                choice = hou.ui.displayMessage("copy or move the cache " + cache.name() + " ?",
                                               severity=hou.severityType.ImportantMessage, buttons=("Copy", "Move", "Cancel"),
                                               close_choice=2, default_choice=2)
                print("choice = " + str(choice))
                if choice != 2:
                    sucess = pullFiles(srcPath, destPath, fileName, choice)
                    if sucess:
                        # rawPath.replace(fileName,
                        cache.parm("file").set(destPath + os.sep + fileName)
                    # update cache path with destPath+fileName
                    print("destPath = " + destPath)
                    print("fileName = " + fileName)
                    print("dirPath = " + srcPath)
    else:
        hou.ui.displayMessage("no caches to pull")