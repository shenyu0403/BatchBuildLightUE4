import os

import perforce
from ..Models.DB import levels_dict, paths_dict

# -----------------------------
# Generate all data needs to know enviroment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = os.path.dirname(paths_dict['UE4 Project'])
lvl_path = lvl_path + "/Content/Scenes/"
lvl_path = os.path.abspath(lvl_path)

revisions = []

# -----------------------------
# Connect to perfoce to check all map (and lvl ussat)
# -----------------------------
def perforcecheckout(levels_used):
    print('Perforce Depot Path >> ', lvl_path)
    p4 = perforce.connect()
    for i in levels_used:
        levels_dict.get(i)
        level = levels_dict[i]
        lvl_name = level[0]
        lvl_end = level[1]
        map = lvl_path + r"\\" + lvl_name + '_' + lvl_end + '/'
        depot = lvl_root + lvl_name + '_' + lvl_end + '/'
        print('Checkout Level >> ', map)

        for filename in os.listdir(os.path.normpath(map)):
            filename = depot + filename
            revisions.append(filename)

        description = """
        [ProVolley][GFX][LightmapAuto] Automatic Build Lightmap generate for the level
        """
        description = description + lvl_name
        cl = p4.findChangelist(description)
        for i in range(len(revisions)):
            file = revisions[i]
            p4.ls(file)
            cl.append(revisions[i])

        revisions.clear()