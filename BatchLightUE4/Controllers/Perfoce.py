import os
import re

from os.path import normpath, abspath, dirname

import perforce
from ..Models.Database import TableProgram


# -----------------------------
# Connect to Perfoce to check all map (and lvl .uasset)
# -----------------------------
def p4_checkout(level_used):
    data = TableProgram()
    data_levels = data.select_levels(name=level_used)
    data_levels = data_levels[0][2]

    regex = r"^.*Perforce"
    lvl_perforce = re.sub(regex, '', data_levels)
    depot = dirname(lvl_perforce)

    p4 = perforce.connect()
    revisions = []

    for filename in os.listdir(dirname(data_levels)):
        filename = '/' + depot + "/" + filename
        if '.uasset' in filename:
            revisions.append(filename)

        if '.umap' in filename:
            revisions.append(filename)

    level_used = level_used.replace('.umap', '')
    description = ("""[ProVolley][GFX][LightmapAuto] Automatic Build """
                   """Lightmap generate for the level """ + level_used)
    cl = p4.findChangelist(description)
    for i in range(len(revisions)):
        file = revisions[i]
        p4.ls(file)
        cl.append(revisions[i])

    revisions.clear()

    return cl


def p4_submit(cl):
    cl.submit()
