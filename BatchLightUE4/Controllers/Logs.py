import os
import sys
import shutil
from ..Models.DB import levels_dict, paths_dict

# This files create a copy of your Unreal log file, useful to see easily
# your rendering errors.

def logsave(level_used):
    level = levels_dict.get(level_used)
    lvl_name = level[0]
    # lvl_end = level[1]

    log_name = lvl_name + ".log"
    root_path = sys.path[0]
    log = paths_dict['UE4 Project']

    src = os.path.dirname(log) + "\Saved\Logs\ProVolley.log"
    src = os.path.normpath(src)
    dst = root_path + r'/Logs/'
    dst = os.path.normpath(os.path.dirname(dst))

    if not os.path.exists(dst):
        os.makedirs(dst)

    dst = dst + '\\' + log_name

    shutil.copyfile(src, dst)
