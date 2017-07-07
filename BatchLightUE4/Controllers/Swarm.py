import os
import json
import psutil
import xml.etree.ElementTree as ET

import subprocess
from ..Models.DB import levels_dict, paths_dict, slave
from BatchLightUE4.Controllers.Logs import logsave

# -----------------------------
# Build level
# -----------------------------
def buildmap(levels_used):
    for i in levels_used:
        levels_dict.get(i)
        level = levels_dict[i]
        lvl_name = level[0]
        lvl_end = level[1]
        ue4_editor = paths_dict['UE4 Editor']
        ue4_project = paths_dict['UE4 Project']
        level = '-map=' + lvl_name + '.umap'
        if lvl_name == 'CharacterCreator':
            level = '-map=' + lvl_end + '.umap'
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
        logsave(lvl_name)

def swarmsetup(bool):
    path_json = os.path.abspath(
        "BatchLightUE4/Models/setup.json")
    path_exe = os.path.dirname(paths_dict['UE4 Editor'])
    os.path.dirname(path_exe)
    path_exe = os.path.dirname(path_exe)
    path_exe = path_exe + '/DotNET'

    path_swarm_setup = path_exe + "/" + "SwarmAgent.Options.xml"


    # --------------------  --------------------
    # Change the Swarm Setup to include all machine selected, need to kill
    # it and relaunch the programm
    if os.path.isfile(path_swarm_setup):
        setup = path_swarm_setup
        setup = ET.parse(setup)
        root = setup.getroot()
        slave_name = str("Agent*, ")
        # for child in setup:
        #     print(child.tag, child.attrib)

        ligne = "AllowedRemoteAgentNames"
        for value in root.iterfind(ligne):
            if bool is True:
                for obj in slave.values():
                    slave_name = slave_name + str(obj[1]) + ", "

            elif bool is False:
                    slave_name = "Agent*"

            new_value = slave_name
            value.text = new_value

        print(path_swarm_setup)
        setup.write(path_swarm_setup)

        kill_it = "SwarmAgent.exe"

        # Kill the programm to relaunch with a new setup
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == kill_it:
                proc.kill()


        # Relaunch the programm
        soft = os.path.abspath(path_exe)
        soft = soft + "/" + kill_it
        subprocess.Popen(soft, stdout=subprocess.PIPE)

    else:
        print("No Setup, generate data")
    # if os.path.isfile(path_json):
    #     with open(path_json) as f:
    #         paths_dict = json.load(f)

    # node xml
    #  - SettableOptions
    #  -- EnableStandaloneMode > False
    #  -- AllowedRemoteAgentNames > AGENT*
    #  -- AllowedRemoteAgentGroup > Default
    #  -- CoordinatorRemotingHost > BUILDER