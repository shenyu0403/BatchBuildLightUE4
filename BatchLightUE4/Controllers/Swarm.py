import os
import psutil
import xml.etree.ElementTree as Element

import subprocess
from ..Models.DB import levels_dict, paths_dict, slave


# -----------------------------
# Build level
# -----------------------------
def build(level_used):
    level = levels_dict.get(level_used)
    lvl_name = level[0]
    lvl_end = level[1]
    ue4_editor = paths_dict['UE4 Editor']
    ue4_project = paths_dict['UE4 Project']
    level = lvl_name + '.umap'
    if lvl_name == 'CharacterCreator':
        level = lvl_end + '.umap'
    subprocess.run([ue4_editor,
                    ue4_project,
                    '-run=resavepackages',
                    '-buildlighting',
                    '-MapsOnly',
                    '-ProjectOnly ',
                    '-AllowCommandletRendering',
                    '-Map=' + level
                    ])


def swarm_setup(boolean):
    path_exe = os.path.dirname(paths_dict['UE4 Editor'])
    os.path.dirname(path_exe)
    path_exe = os.path.dirname(path_exe)
    path_exe = path_exe + '/DotNET'

    path_swarm_setup = path_exe + "/" + "SwarmAgent.Options.xml"

    # --------------------  --------------------
    # Change the Swarm Setup to include all machine selected, need to kill
    # it and relaunch the program
    if os.path.isfile(path_swarm_setup):
        setup = Element.parse(path_swarm_setup)
        root = setup.getroot()
        slave_name = str("Agent*, ")

        line = "AllowedRemoteAgentNames"
        for value in root.iterfind(line):
            # Check the setting, i need to read the config file ; i need to
            # relaunch the setup when i want use a new setting
            if boolean is True:
                for obj in slave.values():
                    slave_name = slave_name + str(obj) + ", "

                if value.text == 'Agent*':
                    value.text = slave_name
                    setup.write(path_swarm_setup)
                    launch_swarm(path_exe)

            elif boolean is False:
                slave_name = "Agent*"

                if value.text != 'Agent*':
                    value.text = slave_name
                    setup.write(path_swarm_setup)
                    launch_swarm(path_exe)

    else:
        print("No Setup, generate data")


def launch_swarm(path_exe):
    kill_it = "SwarmAgent.exe"
    # Kill the program to relaunch with a new setup
    for process in psutil.process_iter():
        # check whether the process name matches
        if process.name() == kill_it:
            process.kill()

    # Relaunch the program
    soft = os.path.abspath(path_exe)
    soft = soft + "/" + kill_it
    subprocess.Popen(soft, stdout=subprocess.PIPE)


def clean_cache_swarm():
    path_exe = os.path.dirname(paths_dict['UE4 Editor'])
    os.path.dirname(path_exe)
    path_exe = os.path.dirname(path_exe)
    path_exe = path_exe + '/DotNET/SwarmCache'

    return path_exe
