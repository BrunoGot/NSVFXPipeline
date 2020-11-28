import os
import hou

def run():
    assetPathFile = r'C:/Users/Natspir/NatspirProd/03_WORK_PIPE/01_ASSET_3D'  # to do : define the pipeline path in a config file. Set possibility to save in or outside the pipeline
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

    # determine the type of the asset by using its path
    if assetPathFile in str(currentPath):
        currentPath = currentPath[len(assetPathFile):]
        splittedPath = currentPath.split('/')
        assetType = splittedPath[1]
        print('assetType =' + assetType)
        assetTask = splittedPath[5]
        assetSubtask = splittedPath[6]
    else:
        pipelineSubPath = ''

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
                assetType = assetInfo[1] + os.sep
            if (assetInfo[2] != ''):
                assetTask = assetInfo[2] + os.sep
            if (assetInfo[3] != ''):
                assetSubtask = assetInfo[3] + os.sep

            pathfile = assetPathFile + os.sep + assetType
            pathfile += assetName + os.sep + pipelineSubPath + assetTask + assetSubtask + 'work_v001' + os.sep

            if (os.path.exists(pathfile) == False):
                os.makedirs(pathfile)
            savedFile = pathfile + assetName + '.hipnc'

            if (os.path.exists(savedFile)):
                # display fucking warning : 'do you want to contine ?'
                print('Waaaaaaarning code this section, a file already exist, save not done')
            else:
                hou.hipFile.save(savedFile)
                hou.ui.displayMessage('Asset saved at ' + savedFile)

