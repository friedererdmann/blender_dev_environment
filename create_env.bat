set BLENDER_ENVIRONMENT=bl_env


if not exist %~dp0%BLENDER_ENVIRONMENT% (
    echo Creating Python Virtual Environment
    echo -      Virtual Environment:  %~dp0%BLENDER_ENVIRONMENT%
    echo.
    python -m venv %BLENDER_ENVIRONMENT%
)

call .\%BLENDER_ENVIRONMENT%\Scripts\Activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt --upgrade
