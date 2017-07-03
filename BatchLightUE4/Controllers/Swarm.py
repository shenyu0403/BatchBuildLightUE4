import os

import subprocess
from ..Models.DB import levels_dict, paths_dict

# -----------------------------
# Build level
# -----------------------------
def buildmap(levels_used):
    for i in levels_used:
        levels_dict.get(i)
        level = levels_dict[i]
        lvl_name = level[0]
        ue4_editor = paths_dict['UE4 Editor']
        ue4_project = paths_dict['UE4 Project']
        level = '-map=' + lvl_name + '.umap'
        print("Buildlight >> ", level)
        subprocess.run([ue4_editor,
                        ue4_project,
                        '-run=resavepackages',
                        '-buildlighting',
                        '-allowcommandletrendering',
                        level,
                        # '-mapstorebuildlightmaps=GYM01.umap',
                        # '-AutomatedMapBuild',
                        ])