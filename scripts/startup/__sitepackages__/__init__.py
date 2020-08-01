import os
import site

env_base_dir = "BASEDIR"
blender_user_scripts = "BLENDER_USER_SCRIPTS"
env_venv_name = "BLENDER_ENVIRONMENT"

base_dir = os.path.abspath(
    os.path.join(
        os.environ.get(
            blender_user_scripts), ".."))
venv_name = os.environ.get(env_venv_name)
PYTHONPATH = os.environ.get('PYTHONPATH', "")

if base_dir and venv_name:
    site_packages = os.path.join(
        base_dir,
        venv_name,
        "lib",
        "site-packages")
    site.addsitedir(site_packages)
    print("\nAdded venv site-packages to site from {0}\n".format(
        site_packages))
else:
    # Fallback in case we can't find the venv
    python_paths = PYTHONPATH.split(";")
    for path in python_paths:
        site.addsitedir(path)
    print("\nAdded paths defined in PYTHONPATH {0} as \
        site package directories\n".format(PYTHONPATH))


def register():
    pass


def unregister():
    pass
