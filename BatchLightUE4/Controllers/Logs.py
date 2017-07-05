import os
import sys
import shutil
from ..Models.DB import paths_dict

# This files create a copy of your Unreal log file, useful to see easily
# your rendering errors.

def logsave(level):
    level = level + ".log"
    root_path = sys.path[0]
    log = paths_dict['UE4 Project']

    src = os.path.dirname(log) + "\Saved\Logs\ProVolley.log"
    src = os.path.normpath(src)
    dst = root_path + r'/Logs/'
    dst = os.path.normpath(os.path.dirname(dst))

    if not os.path.exists(dst):
        os.makedirs(dst)

    print("Log Folder >> ", dst)

    dst = dst + '\\' + level

    shutil.copyfile(src, dst)
