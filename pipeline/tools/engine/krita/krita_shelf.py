import subprocess
#import os
#import pipeline.fileSystem as fs

def save_asset(path_file):
    p = subprocess.Popen([r'C:\Users\Natspir\Documents\Code\Python\AssetManager\venv\Scripts\Python.exe',
                          r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\GUI\save_asset_gui.py',
                          '--path='+path_file, '--ext=kra'], shell=True, stdout=subprocess.PIPE)
    print("test5")
    out = ""
    print("### out process ###")
    #print(p.stdout.readlines())
    print("### end out processs ###")
    for i in p.stdout.readlines():
        print(i)
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
    err = p.stderr.readlines()
    if len(err)>=1:
        print("errors : "+str(err))
        new_path = str(p.stderr.readlines())
    else:
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
    save_asset(r"C:\Users\Natspir\NatspirProd\03_WORK_PIPE\01_ASSET_3D\Concept\MandalaPower\Psyched\Base\006\MandalaPower_006.kra")
    #increment("C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D/Concept/MandalaPower/Psyched/Base/007/MandalaPower_007.kra")
    """import subprocess
        path_file = r"C:\\Users\\Natspir\\NatspirProd\\03_WORK_PIPE\\01_ASSET_3D\\Concept\\MandalaPower\\Psyched\\Base\\006\\MandalaPower_006.kra"
        p = subprocess.Popen([r'C:\\Users\\Natspir\\Documents\\Code\\Python\\AssetManager\\venv\\Scripts\\Python.exe',
                              r'C:\\Users\\Natspir\\Documents\\Code\\Python\\NSVFXPipeline\\pipeline\\tools\\GUI\\save_asset_gui.py',
                              '--path='+path_file, '--ext=kra'], shell=True, stdout=subprocess.PIPE)"""