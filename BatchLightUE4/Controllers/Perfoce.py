import os

import perforce
from ..Models.DB import levels_dict, paths_dict

# -----------------------------
# Generate all data needs to know environment we want build, the stadium
# name, suffix name and -by deduction the path
# -----------------------------
lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
lvl_path = os.path.dirname(paths_dict['UE4 Project'])
lvl_path = lvl_path + "/Content/Scenes/"
lvl_path = os.path.abspath(lvl_path)

revisions = []


# -----------------------------
# Connect to Perfoce to check all map (and lvl .uasset)
# -----------------------------
def perforce_checkout(level_used):
    p4 = perforce.connect()
    # for i in level_used:
    levels_dict.get(level_used)
    level = levels_dict.get(level_used)
    lvl_name = level[0]
    lvl_end = level[1]
    map_build = lvl_path + r"\\" + lvl_name + '_' + lvl_end + '/'
    depot = lvl_root + lvl_name + '_' + lvl_end + '/'
    if lvl_name == 'CharacterCreator':
        map_build = lvl_path + r"\\" + lvl_name + '/'
        depot = lvl_root + lvl_name + '/'

    for filename in os.listdir(os.path.normpath(map_build)):
        filename = depot + filename

        if '.uasset' in filename:
            revisions.append(filename)
        elif '.umap' in filename:
            revisions.append(filename)

    description = """[ProVolley][GFX][LightmapAuto] Automatic Build Lightmap 
    generate for the level """
    description = description + lvl_name
    cl = p4.findChangelist(description)
    for i in range(len(revisions)):
        file = revisions[i]
        p4.ls(file)
        cl.append(revisions[i])

    revisions.clear()

    return cl


def perforce_submit(cl):
    # p4 = perforce.connect()

    # changelist = perforce.models.Changelist(cl)
    cl.submit()
