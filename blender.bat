echo off
set BLENDER="C:\Program Files\Blender Foundation\Blender 2.83\blender.exe"

set BASEDIR=%~dp0
call %~dp0create_env.bat

echo Setting Environment Variables
set BLENDER_USER_SCRIPTS=%BASEDIR%scripts
echo -      BLENDER_USER_SCRIPTS: %BLENDER_USER_SCRIPTS%
echo.

echo Starting Blender
echo -      Blender installation: %BLENDER%
echo -      Startup arguments:    %*
echo.

call %BLENDER% %*
