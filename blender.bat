echo off
set BLENDER_DIR=C:\Program Files\Blender Foundation\Blender 2.90
set BLENDER="%BLENDER_DIR%\blender.exe"
set BLENDER_PYTHON="%BLENDER_DIR%\2.90\python\bin"

set PATH=%BLENDER_PYTHON%;%PATH%
call "%~dp0create_env.bat"

echo Setting Environment Variables
set BLENDER_USER_SCRIPTS=%~dp0scripts
echo -      BLENDER_USER_SCRIPTS: %BLENDER_USER_SCRIPTS%
echo.

echo Starting Blender
echo -      Blender installation: %BLENDER%
echo -      Startup arguments:    %*
echo.

call %BLENDER% %*
