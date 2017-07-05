import os
import shutil
from ..Models.DB import paths_dict

# This files create a copy of your Unreal log file, useful to see easily
# your rendering errors.

def logsave(level):
    level = level + ".log"
    path_saved = os.path.realpath(__file__)
    log = paths_dict['UE4 Project']

    src = os.path.dirname(log) + "\Saved\Logs\PProVolley.log"
    dst = os.path.dirname(path_saved) + r'/Logs/' + level
    dst = os.path.normpath(dst)

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    print("src > ", src)
    print("dst > ", dst)
    shutil.copyfile(src, dst)


test = "truc"

logsave(test)
