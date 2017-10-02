import tkinter as tk
import tkinter.filedialog as tkfile
import tkinter.messagebox as msg

import os
import sys
import json
import perforce

from ..Models.DB import levels_dict, paths_dict
from ..Controllers.Logs import log_save
from ..Controllers.Network import SaveNetworkName
from ..Controllers.Perfoce import perforce_checkout
from ..Controllers.Swarm import build, swarm_setup


# --------
# UI
# --------
class UIBuildMap(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.env_names = levels_dict
        self.labelVariable = tk.StringVar()
        self.buttons = {}
        self.value_check = [0]
        self.check_state = tk.NORMAL
        for i in levels_dict.keys():
            self.value_check.append(i)

        self.value_swarm = tk.BooleanVar(self, '0')

        # Define Icon
        self.icon_log = 'BatchLightUE4/Resources/log.gif'
        self.icon_trash = 'BatchLightUE4/Resources/trash.gif'

        self.initialize()

    def initialize(self):
        self.grid()

        # ------------------------------------------------
        # BatchBuild Program

        path_icon = os.path.abspath(
            "BatchLightUE4/Resources/BlackSheep.ico")
        if os.path.isfile(path_icon) is not False:
            self.iconbitmap(path_icon)

        tk.Button(self, text=u'Selected All', command=self.select_all).grid(
            column=0, row=0, padx=5, pady=5, sticky='EW')
        tk.Button(self, text=u'Unselected All',
                  command=self.unselected_all).grid(column=1, row=0, padx=5,
                                                    pady=5, sticky='EW')

        frame_lvl = tk.LabelFrame(self,
                                  text="All Levels",
                                  padx=5,
                                  pady=5)
        frame_lvl.grid(columnspan=2)

        label = tk.Label(self, textvariable=self.labelVariable, anchor='w')
        label.grid(sticky='EW')

        tk.Label(frame_lvl, text='---- Gymnasium', anchor='w').grid(
            columnspan=2, sticky='EW')

        lvl_root = '//ProVolley/UnrealProjects/ProVolley/Content/Scenes/'
        p4 = perforce.connect()
        env_names = self.env_names
        for cle, level in env_names.items():
            # ---------- Check if the level can be Checkout or not
            lvl_name = level[0]
            lvl_end = level[1]
            filename = lvl_root + lvl_name
            filename = filename + '_' + lvl_end + '/' + lvl_name + '.umap'
            if lvl_name == 'CharacterCreator':
                filename = lvl_root + lvl_name + '/' + lvl_end + '.umap'
            filename = perforce.Revision(p4, filename)

            if filename.openedBy == str(1):
                self.check_state = tk.DISABLED

            # ---------- Generate a checkbox Widget
            self.value_check[cle] = tk.BooleanVar(self, '0')
            self.buttons[cle] = tk.Checkbutton(frame_lvl,
                                               text=level,
                                               variable=self.value_check[cle],
                                               anchor='w',
                                               state=self.check_state)
            self.buttons[cle].grid(columnspan=2, sticky='EW')

            if level[0] == 'GYM02':
                tk.Label(frame_lvl, text='---- Stadium', anchor='w').grid(
                    columnspan=2, sticky='EW')

            if level[0] == 'STA09':
                tk.Label(frame_lvl, text='---- Training Cour',
                         anchor='w').grid(
                    columnspan=2, sticky='EW')

            if level[0] == 'TC02':
                tk.Label(frame_lvl, text='---- Extra Levels',
                         anchor='w').grid(
                    columnspan=2, sticky='EW')

        # ------------------------------------------------
        # Launch Program
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        tk.Button(self,
                  text=u'Build Light',
                  command=self.on_button_click).grid(sticky='EW',
                                                     column=0,
                                                     row=3,
                                                     padx=5,
                                                     pady=5, )

        swarm_btn = tk.Checkbutton(self,
                                   text="All",
                                   variable=self.value_swarm,
                                   anchor='w',)
        swarm_btn.grid(column=1, row=3, sticky='EW')

        # ------------------------------------------------
        # Setup path
        frame_setup = tk.LabelFrame(self,
                                    text="Setup Path",
                                    padx=5,
                                    pady=5)
        frame_setup.grid(columnspan=2)

        text = paths_dict["UE4 Editor"]
        ue4_path_text = tk.StringVar(self, value=text)
        ue_4_path = tk.Entry(frame_setup,
                             textvariable=ue4_path_text)
        ue_4_path.grid(column=0, row=1, sticky='EW', padx=5, pady=5)
        ue_4_btn = tk.Button(frame_setup,
                             text=u'UE4Editor.exe',
                             command=lambda: self.open_file(ue4_path_text, 1))
        ue_4_btn.grid(column=1, row=1, sticky='EW', padx=5, pady=5)

        text = paths_dict["UE4 Project"]
        ue4_project_text = tk.StringVar(self, value=text)
        project_path = tk.Entry(frame_setup,
                                textvariable=ue4_project_text,)
        project_path.grid(column=0, row=2, sticky='EW', padx=5, pady=5)
        project_btn = tk.Button(frame_setup,
                                text=u'Uproject',
                                command=lambda: self.open_file(
                                   ue4_project_text,
                                   2))
        project_btn.grid(column=1, row=2, sticky='EW', padx=5, pady=5)

        # ------------------------------------------------
        # Log options
        frame_log = tk.LabelFrame(self,
                                  text="Log Options",
                                  padx=5,
                                  pady=5)
        frame_log.grid(columnspan=2)
        self.icon_log = tk.PhotoImage(file='BatchLightUE4/Resources/log.gif')
        log_open_folder = tk.Button(frame_log,
                                    image=self.icon_log,
                                    text=u'Open log folder',
                                    compound=tk.LEFT,
                                    command=self.LogOpenFolder)
        log_open_folder.grid(column=0, row=5, sticky='EW', padx=5, pady=5)

        self.icon_trash = tk.PhotoImage(file=self.icon_trash)
        log_trash = tk.Button(frame_log,
                              image=self.icon_trash,
                              text='Clean Log',
                              compound=tk.LEFT,
                              command=self.LogCleanFolder)
        log_trash.grid(column=1, row=5, sticky='EW', padx=5, pady=5)

        # ------------------------------------------------
        # Network Setup
        frame_network = tk.LabelFrame(self,
                                      text="Network Setup", padx=5, pady=5)
        frame_network.grid()
        run_save_network = tk.Button(frame_network,
                                     text=u'Save network Name',
                                     command=self.runNetwork)
        run_save_network.grid()

    # ------------------------------------------------
    # Event and Command
    def select_all(self):
        for cle in self.buttons.keys():
            dict_state = self.buttons[cle].config('state')
            if dict_state[4] == 'normal':
                print(cle)
                self.buttons[cle].select()

        self.labelVariable.set("Select all Levels")

    def unselected_all(self):
        for cle in self.buttons.keys():
            self.buttons[cle].deselect()
        self.labelVariable.set("Clear list selection")

    @staticmethod
    def open_file(variable, id_dict):
        # textfield = variable.get()
        textfield = tkfile.askopenfilename()

        if id_dict == 1:
            paths_dict["UE4 Editor"] = textfield
        elif id_dict == 2:
            paths_dict["UE4 Project"] = textfield
        elif id_dict == 3:
            paths_dict["Swarm"] = textfield

        variable.set(textfield)
        path_json = os.path.abspath(
            "BatchLightUE4/Models/setup.json")
        with open(path_json, 'w') as f:
            json.dump(paths_dict, f, indent=4)
        # print(textfield, id)

    # ------------------------------------------------
    # All log option, open folder and delete file
    def LogOpenFolder(self):
        path_log = sys.path[0] + '\\Logs\\'
        os.system("explorer " + path_log)

        text = "Log Folder"
        self.labelVariable.set(text)

    def LogCleanFolder(self):
        text = "Delete Log Folder"
        self.labelVariable.set(text)

        path_exe = os.path.dirname(paths_dict['UE4 Editor'])
        os.path.dirname(path_exe)
        path_exe = os.path.dirname(path_exe)
        path_exe = os.path.abspath(path_exe + '/DotNET/SwarmCache/')

        os.remove(path_exe)

        print("Delete log, path exe :")
        print(path_exe)

    # ------------------------------------------------
    # Menu command
    def runNetwork(self):
        print('Hello World')

        SaveNetworkName()

    def exit(self):
        print('Tchuss')

        # exit(self)

    # --------------------  --------------------
    # This function call perforce and swarm to check out all file and build
    # all level choice
    def on_button_click(self):
        # Generate empty Data
        levels_rendering = []
        text = ""

        for key, value in self.buttons.items():
            check = self.value_check[key].get()
            if check is True:
                levels_rendering.append(key)
                nbr = len(levels_rendering)
                text = "Build "
                text = text + str(nbr) + " level(s)"
            elif len(levels_rendering) == 0:
                text = "Empty Choice"

        self.labelVariable.set(text)

        # --------------------  --------------------
        # Windows to launch the calculation process, simple loop to launch
        # all process, one after one :
        #   - Fisrt step disable -temporarily- the hibernate mode with a
        # simple windows command.
        #   - Check if the Swarm need to be relaunch with a special setup
        #   - Checkout the level we want build
        #   - Now we can build the level
        #   - New Loop and retarst to the Checkout loop.
        if msg.askyesno('Launch Build', 'Lancement du calcul ?'):
            # os.system('powercfg -h off')
            # print(os.system('powercfg -h off'))

            swarm_setup(self.value_swarm.get())

            for level_build in levels_rendering:
                level = levels_dict.get(level_build)
                lvl_name = level[0]
                print("Build Level >> ", lvl_name)

                perforce_checkout(level_build)
                build(level_build)
                log_save(level_build)

        levels_rendering = []
        swarm_setup(False)
        print("All levels selected are rendering and checkout")

