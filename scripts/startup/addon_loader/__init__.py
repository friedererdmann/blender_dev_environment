import sys
import os
import json
import bpy
import addon_utils
from bpy.app.handlers import persistent


class addon_config():
    def __init__(self, name="", repo="", enable=True, persistent=True, startup=False, code=""):
        self.name = name
        self.repo = repo
        self.enable = enable
        self.persistent = persistent
        self.startup = startup
        self.code = code


def get_addon_configurations():
    env_base_dir = "BASEDIR"
    base_dir = os.environ.get(env_base_dir)
    config_file = "addons.json"
    if not base_dir:
        print("Couldn't find {0} environment variable.".format(env_base_dir))
        return []
    addon_file = os.path.join(base_dir, config_file)
    if not os.path.exists(addon_file):
        print("Couldn't find {0} file in {1}.".format(config_file, base_dir))
        return []
    with open(addon_file) as json_file:
        try:
            addon_configurations = [addon_config(**x) for x in json.load(json_file)]
        except json.decoder.JSONDecodeError as e:
            print("Json decoding issue in {0}\n\
                File couldn't be read correctly.\n\
                Error message:\n{1}".format(config_file,e))
            return []
        except TypeError as e:
            print("Type issue in {0}\n\
                We except the a list of configurations.\n\
                Configurations should be of type addon_config.\n\
                Error message:\n{1}".format(config_file,e))
            return []
    return addon_configurations


addon_configurations = get_addon_configurations()


def paths():
    global addon_configurations
    # RELEASE SCRIPTS: official scripts distributed in Blender releases
    addon_paths = bpy.utils.script_paths("addons")

    # CONTRIB SCRIPTS: good for testing but not official scripts yet
    # if folder addons_contrib/ exists, scripts in there will be loaded too
    addon_paths += bpy.utils.script_paths("addons_contrib")

    for addon in addon_configurations:
        if addon.repo and addon.repo not in addon_paths:
            addon_paths.append(addon.repo)

    return addon_paths


addon_utils.paths = paths


@persistent
def load_addons(self):
    global addon_configurations
    addon_paths = addon_utils.paths()

    print("\nThe following paths are now being considered for Addons:")
    for i, addon_path in enumerate(addon_paths):
        path = os.path.normpath(addon_path)
        print("\t{0:02d} {1}".format(i, path))

    print("\nNow loading the following plugins:")
    for i, addon in enumerate(addon_configurations):
        if addon.name:
            print("\n\t{0:02d} {1}".format(i, addon.name))
            if addon.startup:
                print("\t\tExecuting the following code:")
                [print("\t\t\t",line) for line in addon.code.split(";")]
                exec(addon.code)
            if addon.enable:
                addon_utils.enable(
                            module_name = addon.name,
                            persistent = addon.persistent,
                            default_set = False)


bpy.app.handlers.load_post.append(load_addons)


def register():
    pass


def unregister():
    pass
