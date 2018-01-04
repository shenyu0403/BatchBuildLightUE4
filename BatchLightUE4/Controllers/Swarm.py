import os
import psutil
import xml.etree.ElementTree as Element
import json
import subprocess

from os.path import exists, expanduser, join
from BatchLightUE4.Models.Database import TableProgram


def build(level_used):
    """
    Build all selected levels. Need a list with all level name.
    - level_used : List contains all level you want calculate.

    :param level_used: the level name. This data has send to the swarm
    process
    :type level_used: basestring
    :return The process ID, wait to communicate it
    """
    paths = TableProgram().select_path(1)
    ue4_editor = paths[0][1]
    ue4_project = paths[0][2]
    swarm = subprocess.Popen([ue4_editor,
                              ue4_project,
                              '-run=resavepackages',
                              '-buildlighting',
                              '-AllowCommandletRendering',
                              '-MapsOnly',
                              '-ProjectOnly',
                              '-map=' + level_used])

    return swarm


def swarm_setup(boolean):
    """Change your setup with all parameter."""
    path_ue4 = TableProgram().select_path(1)
    path_exe = os.path.dirname(path_ue4[0][1])
    os.path.dirname(path_exe)
    path_exe = os.path.dirname(path_exe)
    path_exe = path_exe + '/DotNET'

    path_swarm_setup = path_exe + "/" + "SwarmAgent.Options.xml"

    network_dict = 'network.json'
    network_path = join(expanduser('~'), 'BBLUE4', network_dict)

    if exists(network_path):
        with open(network_path, 'r') as f:
            slave = json.load(f)

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
    path_ue4 = TableProgram().select_path(1)
    path_exe = os.path.dirname(path_ue4[1])
    os.path.dirname(path_exe)
    path_exe = os.path.dirname(path_exe)
    path_exe = path_exe + '/DotNET/SwarmCache'

    return path_exe
