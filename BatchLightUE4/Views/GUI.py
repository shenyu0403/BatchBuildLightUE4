import tkinter as tk
import tkinter.filedialog as tkfile
import tkinter.messagebox as msg
import json
import os
import perforce
from ..Models.DB import levels_dict, paths_dict
from ..Controllers.Perfoce import perforcecheckout
from ..Controllers.Swarm import buildmap, swarmsetup

# --------
# UI
# --------
class UIBuildMap(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.env_names = levels_dict
        self.buttons = {}
        self.value_checkbox = [0]
        for i in levels_dict.keys():
            self.value_checkbox.append(i)
        self.initialize()

    def initialize(self):
        self.grid()
        path_icon = os.path.abspath(
            "BatchLightUE4/Ressources/BlackSheep.ico")
        if os.path.isfile(path_icon) is not False:
            self.iconbitmap(path_icon)

        tk.Button(self, text=u'Select All', command=self.SelectAll).grid(
            column=0, row=0, padx=5, pady=5, sticky='EW')
        tk.Button(self, text=u'Unselect All',
                  command=self.UnSelectAll).grid(column=1, row=0, padx=5,
                                                 pady=5, sticky='EW')

        frame_lvl = tk.LabelFrame(self,
                                  text="All Levels",
                                  padx=5,
                                  pady=5)
        frame_lvl.grid(columnspan=2)

        self.labelVariable = tk.StringVar()
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
            filename = lvl_root + lvl_name + '_' + lvl_end + '/' + lvl_name \
                       + '.umap'
            if lvl_name == 'CharacterCreator':
                filename = lvl_root + lvl_name + '/' + lvl_end + '.umap'
            filename = perforce.Revision(p4, filename)

            if filename.openedBy == str(1):
                self.checkstate = tk.DISABLED
            else:
                self.checkstate = tk.NORMAL

            # ---------- Generate a checkbox Widget
            self.value_checkbox[cle] = tk.BooleanVar(self, '0')
            self.buttons[cle] = tk.Checkbutton(frame_lvl,
                                               text=level,
                                               variable=self.value_checkbox[cle],
                                               anchor='w',
                                               state=self.checkstate)
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
        # Launch Programm
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        tk.Button(self,
                  text=u'Build Light',
                  command=self.OnButtonClick).grid(sticky='EW',
                                                   column=0,
                                                   row=3,
                                                   padx=5,
                                                   pady=5,)

        self.value_swarm = tk.BooleanVar(self, '0')
        self.swarmBTN = tk.Checkbutton(self,
                                       text="All",
                                       variable=self.value_swarm,
                                       anchor='w',)
        self.swarmBTN.grid(column=1,row=3, sticky='EW')

        # ------------------------------------------------
        # Setup path
        frame_setup = tk.LabelFrame(self,
                                    text="Setup Path",
                                    padx=5,
                                    pady=5)
        frame_setup.grid(columnspan=2)

        text = paths_dict["UE4 Editor"]
        self.UE4Path_text = tk.StringVar(self, value=text)
        UE4Path = tk.Entry(frame_setup,
                           textvariable=self.UE4Path_text)
        UE4Path.grid(column=0, row=1, sticky='EW', padx=5, pady=5)
        UE4Btn = tk.Button(frame_setup,
                           text=u'UE4Editor.exe',
                           command=lambda: self.OpenFilExe(
                               self.UE4Path_text,
                               1))
        UE4Btn.grid(column=1, row=1, sticky='EW', padx=5, pady=5)

        text = paths_dict["UE4 Project"]
        self.UE4Project_text = tk.StringVar(self, value=text)
        ProjectPath = tk.Entry(frame_setup,
                               textvariable=self.UE4Project_text,)
        ProjectPath.grid(column=0, row=2, sticky='EW', padx=5, pady=5)
        ProjectBtn = tk.Button(frame_setup,
                               text=u'Uproject',
                               command=lambda: self.OpenFilExe(
                                   self.UE4Project_text,
                                   2))
        ProjectBtn.grid(column=1, row=2, sticky='EW', padx=5, pady=5)

        # text = paths_dict["Swarm"]
        # self.SAPath_text = tk.StringVar(self, value=text)
        # SAPath = tk.Entry(frame_setup,
        #                   textvariable=self.SAPath_text)
        # SAPath.grid(column=0, row=3, sticky='EW', padx=5, pady=5)
        # SABtn = tk.Button(frame_setup,
        #                   text=u'SwarmAgent.exe',
        #                   command=lambda: self.OpenFilExe(self.SAPath_text,
        #                                                   3))
        # SABtn.grid(column=1, row=3, sticky='EW', padx=5, pady=5)

        # ------------------------------------------------
        # Swarm Setup
        # frame_swarm = tk.LabelFrame(self,
        #                           text="Swarm Agent",
        #                           padx=5,
        #                           pady=5)
        # frame_swarm.grid(columnspan=2)
        # self.value_swarm = tk.BooleanVar(self, '0')
        #
        # self.swarmBTN = tk.Checkbutton(frame_swarm,
        #                                text="Activate Global Swarm Setup",
        #                                variable=self.value_swarm,
        #                                anchor='w',)
        # self.swarmBTN.grid(columnspan=2, sticky='EW')

        # self.swarmSetup = tk.Button(frame_swarm, text="Setup Swarm",
        #                             command=self.OpenWindow)
        # self.swarmSetup.grid(columnspan=2, sticky='EW')

        # ------------------------------------------------
        # Event and Command
    def SelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].select()
        self.labelVariable.set("Select all Levels")

    def UnSelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].deselect()
        self.labelVariable.set("Clear list selection")

    def OpenFilExe(self, variable, id):
        # textfield = variable.get()
        textfield = tkfile.askopenfilename()

        if id == 1:
            paths_dict["UE4 Editor"] = textfield
        elif id == 2:
            paths_dict["UE4 Project"] = textfield
        elif id == 3:
            paths_dict["Swarm"] = textfield

        variable.set(textfield)
        path_json = os.path.abspath(
            "BatchLightUE4/Models/setup.json")
        with open(path_json, 'w') as f:
            json.dump(paths_dict, f, indent=4)
        # print(textfield, id)

    # def OpenWindow(self):
    #     print("Swarm Setup")
    #     tk.Toplevel(SwarmUI)

    # --------------------  --------------------
    # This function call perforce and swarm to check out all file and build
    # all level choiced
    def OnButtonClick(self):
        # Generate empty Data
        levels_rendering = []
        text = ""

        for key, value in self.buttons.items():
            check = self.value_checkbox[key].get()
            if check is True:
                levels_rendering.append(key)
                nbr = len(levels_rendering)
                text = "Build "
                text = text + str(nbr) + " level(s)"
            elif len(levels_rendering) == 0:
                text = "Empty Choice"

        self.labelVariable.set(text)
        if msg.askyesno('Launch Build', 'Lancement du calcul ?'):
            swarm_statut = self.value_swarm.get()
            # if swarm_statut == True:
            swarmsetup(swarm_statut)

            perforcecheckout(levels_rendering)
            buildmap(levels_rendering)

        levels_rendering = []
        swarmsetup(False)
        print("All levels selected are rendering and checkout")

