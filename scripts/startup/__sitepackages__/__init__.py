import os
import site


PYTHONPATH = os.environ['PYTHONPATH'].split(";")[0]
site.addsitedir(PYTHONPATH)
print("\nAdded PYTHONPATH {0} as site package directory\n".format(PYTHONPATH))


def register():
    pass


def unregister():
    pass
