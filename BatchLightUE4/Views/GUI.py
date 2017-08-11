import tkinter as tk
import tkinter.filedialog as tkfile
import tkinter.messagebox as msg

import os, sys, json, perforce

from ..Models.DB import levels_dict, paths_dict
from ..Controllers.Logs import logsave
from ..Controllers.Network import SaveNetworkName
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
        # ------------------------------------------------
        # Topbar Menu
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        self.filemenu = tk.Menu(self.menubar)
        self.filemenu.add_command(label="New", command=self.popup())
        self.filemenu.add_command(label="Open", command=self.popup())
        self.menubar.add_cascade(label="File", menu=self.filemenu)


        # ------------------------------------------------
        # BatchBuild Programm

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

        # ------------------------------------------------
        # Log options
        frame_log = tk.LabelFrame(self,
                                    text="Log Options",
                                    padx=5,
                                    pady=5)
        frame_log.grid(columnspan=2)
        self.icon_log = tk.PhotoImage(file='BatchLightUE4/Ressources/log.gif')
        LogOpenFolder = tk.Button(frame_log,
                                  image=self.icon_log,
                                  text=u'Open log folder',
                                  compound=tk.LEFT,
                                  command=self.LogOpenFolder)
        LogOpenFolder.grid(column=0, row=5, sticky='EW', padx=5, pady=5)

        self.icon_trash = tk.PhotoImage(
            file='BatchLightUE4/Ressources/trash.gif')
        LogTrash = tk.Button(frame_log,
                             image=self.icon_trash,
                             text='Clean Log',
                             compound=tk.LEFT,
                             command=self.LogCleanFolder)
        LogTrash.grid(column=1, row=5, sticky='EW', padx=5, pady=5)

        # ------------------------------------------------
        # Network Setup
        frame_network = tk.LabelFrame(self,
                                    text="Network Setup",
                                    padx=5,
                                    pady=5)
        frame_network.grid()
        runSaveNetwork = tk.Button(frame_network,
                                  text=u'Save network Name',
                                  command=self.runNetwork)
        runSaveNetwork.grid()

    # ------------------------------------------------
    # Topbar Menu
    def popup(self):
        print('test')

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
    # Network Event
    def runNetwork(self):
        print('Hello World')

        SaveNetworkName()


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

            swarmsetup(self.value_swarm.get())

            for level_build in levels_rendering:
                level = levels_dict.get(level_build)
                lvl_name = level[0]
                print("Build Level >> ", lvl_name)

                perforcecheckout(level_build)
                buildmap(level_build)
                logsave(level_build)

            # os.system('powercfg -h on')
            # print(os.system('powercfg -h on'))

        levels_rendering = []
        swarmsetup(False)
        print("All levels selected are rendering and checkout")

