import os
import subprocess

def run():
    #print("test")
    path_file = ""#hou.hipFile.path()
    p = subprocess.Popen([r'C:\Program Files\Side Effects Software\Houdini 18.5.408\python27\python.exe',
                          r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\pipeline\tools\GUI\save_asset_gui.py',
                          '--path=' + path_file, '--ext=kra'], shell=True, stderr=subprocess.PIPE)
    """assetPathFile = fs.asset_base_path   # to do : define the pipeline path in a config file. Set possibility to save in or outside the pipeline
    pipelineSubPath = os.sep + '3d' + os.sep + 'scenes' + os.sep
    assetName = hou.hipFile.basename()

    #remove the extenction of the file
    extenction = assetName.split(".")[-1]
    assetName = assetName.replace("."+extenction, "")

    currentPath = hou.hipFile.path()
    print('currentPath = ' + str(currentPath) + " pathfile = " + assetPathFile)
    assetType = ''
    assetTask = ''
    assetSubtask = ''
    assetVersion = 'work_v001'

    #fill the information using the path
    if assetPathFile in str(currentPath):
        currentPath = currentPath[len(assetPathFile)+1:]
        cur_path_test = os.path.dirname(currentPath)
        cur_path_test = cur_path_test.replace('/', "\\")
        datas = fs.get_datas_from_path(cur_path_test)
        if datas!=None:
            assetType = datas['AssetType']
            assetTask = datas['Task']
            assetSubtask = datas['Subtask']
            print(datas)

    message = "test"
    inputUser = hou.ui.readMultiInput(message, ('Asset Name', 'Asset Type', 'Task', 'Subtask'), buttons=('Cancel', 'OK'),
                                      default_choice=1, initial_contents=(assetName, assetType, assetTask, assetSubtask))
    print('inputUser =' + str(inputUser[0]))
    if (inputUser[0] == 1):
        assetInfo = inputUser[1]
        print('length inputUser = ' + str(len(assetInfo)))
        print('asset type = ' + assetInfo[0])
        if (assetInfo[0] == ''):
            hou.ui.displayMessage('You must set an asset name. Asset not saved', severity=hou.severityType.Warning)
        else:
            assetName = assetInfo[0]
            # if the other fields are empty don't put it in  the pipeline file
            if (assetInfo[1] != ''):
                assetType = assetInfo[1]
            if (assetInfo[2] != ''):
                assetTask = assetInfo[2]
            if (assetInfo[3] != ''):
                assetSubtask = assetInfo[3]

            pipe_path = fs.get_path({"AssetType":assetType, "AssetName":assetName, "Task":assetTask, "Subtask":assetSubtask, "Version":assetVersion })
            #soon depreciated
            pathfile = assetPathFile + os.sep + pipe_path+os.sep
            #pathfile += assetName + os.sep + pipelineSubPath + assetTask + assetSubtask + assetVersion + os.sep
            print("pipe_path = "+pathfile)

            if (os.path.exists(pathfile) == False):
                os.makedirs(pathfile)
            savedFile = pathfile + assetName + '.hipnc'

            if (os.path.exists(savedFile)):
                # display fucking warning : 'do you want to contine ?'
                print('Waaaaaaarning code this section, a file already exist, save not done')
            else:
                hou.hipFile.save(savedFile)
                hou.ui.displayMessage('Asset saved at ' + savedFile)"""

if __name__ == "__main__":
    p = subprocess.Popen([r'C:\Users\Natspir\Documents\Code\Python\NSVFXPipeline\dist\save_asset_gui.exe',
                          '--path=C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D\\Save_as\\Pipeline_Test\\Blender\\Deployment_Test\\001\\MandalaPower_007.blend', '--ext=blend'], shell=False, stdout=subprocess.PIPE)

    print("test")