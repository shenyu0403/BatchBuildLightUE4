import os
import re

import perforce
from ..Models.projects import TableProgram

# -----------------------------
# Generate all data needs to know environment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
data_paths = TableProgram().select_path(1)
data_levels = TableProgram().select_levels()
# Simple fix to work with Perforce ! Need to be upgrade
path_perforce = '//ProVolley/'
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = os.path.dirname(data_paths[0][2])
lvl_path = lvl_path + "/Content/Scenes/"
lvl_path = os.path.abspath(lvl_path)


# -----------------------------
# Connect to Perfoce to check all map (and lvl .uasset)
# -----------------------------
def perforce_checkout(level_used):
    revisions = []
    p4 = perforce.connect()
    data_levels = TableProgram().select_levels(name=level_used)
    data_levels = os.path.abspath(data_levels[0][2])

    regex = r"^.*Perforce"
    lvl_perforce = re.sub(regex, '', data_levels)

    # map_build = lvl_path + r"\\" + level_used + '/'
    depot = os.path.dirname(lvl_perforce)

    for filename in os.listdir(os.path.dirname(data_levels)):
        filename = depot + "\\" + filename

        if '.uasset' in filename:
            revisions.append(filename)
        elif '.umap' in filename:
            revisions.append(filename)

    print('test')
    description = """[ProVolley][GFX][LightmapAuto] Automatic Build Lightmap 
    generate for the level """
    level_used = level_used.replace('.umap', '')
    description = description + level_used
    cl = p4.findChangelist(description)
    for i in range(len(revisions)):
        file = revisions[i]
        p4.ls(file)
        cl.append(revisions[i])

    revisions.clear()

    return cl


def perforce_submit(cl):
    cl.submit()
