echo off
set BLENDER="C:\Program Files\Blender Foundation\Blender 2.83\blender.exe"

set BLENDER_ENVIRONMENT=bl_env
set BASEDIR=%~dp0
SET VENV=%BASEDIR%%BLENDER_ENVIRONMENT%
if not exist "%VENV%" (
    echo Creating Python Virtual Environment
    echo -      Virtual Environment:  %VENV%
    echo.
    call create_env.bat
)

echo Setting Environment Variables
set PYTHONPATH=%VENV%\lib\site-packages\
set BLENDER_USER_SCRIPTS=%BASEDIR%scripts
echo -      PYTHONPATH:           %PYTHONPATH%
echo -      BLENDER_USER_SCRIPTS: %BLENDER_USER_SCRIPTS%
echo.

echo Starting Blender
echo -      Blender installation: %BLENDER%
echo -      Startup arguments:    %*
echo.

call %BLENDER% %*
