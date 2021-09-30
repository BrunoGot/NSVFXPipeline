import subprocess
#import os
#import pipeline.fileSystem as fs

def save_asset(path_file):
    p = subprocess.Popen([r'C:\Users\Natspir\Documents\Code\Python\AssetManager\venv\Scripts\Python.exe',
                          r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\GUI\save_asset_gui.py',
                          '--path='+path_file], shell=True, stdout=subprocess.PIPE)
    print("test5")
    out = ""
    print("### out process ###")
    #print(p.stdout.readlines())
    print("### end out processs ###")
    for i in p.stdout.readlines():
        #print("aaa")
        if b"save path_id" in i:
            out = str(i)
            #cleaning out string :
            out = out.split("=")
            out = out[1]
            out = out.replace(r"\r\n'", "")
            out = out.replace(" ","")
    print("out = "+out)
    return out

def cleaning(out_bstring):
    out = str(out_bstring)
    out = out.split("=")
    out = out[1]
    out = out.replace(r"\r\n'", "")
    out = out.replace(" ", "")
    return out

def increment(path_file):
    p = subprocess.Popen([r'C:\Users\Natspir\Documents\Code\Python\AssetManager\venv\Scripts\Python.exe',
                          r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\engine\increment.py',
                          '--path=' + path_file], shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    new_path = ""
    out = p.stdout.readlines()
    for i in out:
        print(i)
        if b'new_path =' in i:
            new_path = i
            new_path = cleaning(new_path)
            print("path found, new_path = "+new_path)

    return new_path
    #get the datas from the path
    """datas = fs.get_datas_from_path(path_file)
    print("datas = "+str(datas))
    #if datas are valids :
    if datas :
        digit_version = datas["Version"]
        folder_name = fs.conf.version.format({"Version":digit_version})
        exist = True
        new_path = path_file
        while exist == True:
            #convert to in, increment it, then convert it back to string
            digit_version = int(digit_version,)
            digit_version+=1
            digit_version = f"{digit_version:03}"
            #update the datas with the new work iteration
            datas["Version"] = digit_version
            new_path = fs.get_path(datas)
            #if the path doesn't exist yet, it's ok let's break the loop, else go for a new iteration
            if not os.path.exists(new_path):
                exist = False
        print("new_path = "+new_path)"""

        #print("digit = "+digit)

    #   increment work folder
    #   remake new_path
    #   return new_path

if __name__=="__main__":
    save_asset("")
    #increment("C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D/Concept/Test/Task_Test/Subtask_Test/work_005/Test_work_005.kra")
    """krita code : 
    from pipeline.tools.engine.krita import krita_shelf as shelf
import importlib
importlib.reload(shelf)
doc = Krita.instance().activeDocument()
if doc:
    path_id = shelf.save_asset(doc.fileName())
    if path_id != "":
        print("path_id = "+path_id)
        name =path_id#"C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D/Test/Test/Test/Test/001"
        name += ".kra"
        doc.saveAs(name)
    
    """
"""fileName = QFileDialog.getSaveFileName()[0]
print("filename = "+fileName)
print("file_name = "+file_name)
# And export the document to the fileName location.
# InfoObject is a dictionary with specific export options, but when we make an empty one Krita will use the export defaults.
doc.exportImage(file_name, InfoObject())"""