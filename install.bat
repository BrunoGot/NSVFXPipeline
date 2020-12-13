SET mypath=%~dp0
echo %mypath:~0,-1%
SET pipeline_path=%~dp0pipeline\tools\engine\houdini\launch";&HOUDINI_SCRIPT_PATH;&;"
echo %pipeline_path%
setx HOUDINI_SCRIPT_PATH %pipeline_path%

pause