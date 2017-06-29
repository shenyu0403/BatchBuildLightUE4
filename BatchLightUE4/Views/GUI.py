import tkinter as tk
import tkinter.filedialog as tkfile
import tkinter.messagebox as msg
import json
import os
from ..Models.DB import levels_dict, levels_rendering, paths_dict
from ..Controllers.BuildLightUE4 import perforcecheckout, buildmap

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

        env_names = self.env_names
        for cle, level in env_names.items():
            self.value_checkbox[cle] = tk.BooleanVar(self, '0')
            self.buttons[cle] = tk.Checkbutton(frame_lvl, text=level,
                                                variable=self.value_checkbox[cle],
                                                anchor='w')
            self.buttons[cle].grid(columnspan=2, sticky='EW')

            if level[0] == 'GYM02':
                tk.Label(frame_lvl, text='---- Stadium', anchor='w').grid(
                    columnspan=2, sticky='EW')

            if level[0] == 'STA09':
                tk.Label(frame_lvl, text='---- Training Cour',
                         anchor='w').grid(
                    columnspan=2, sticky='EW')

        # ------------------------------------------------
        # Launch Programm
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        tk.Button(self,
                  text=u'Build Light',
                  command=self.OnButtonClick).grid(columnspan=2,
                                                   sticky='EW',padx=5, pady=5,)

        # ------------------------------------------------
        # Setup path
        text = paths_dict["UE4 Editor"]
        self.UE4Path_text = tk.StringVar(self, value=text)
        UE4Path = tk.Entry(self,
                           textvariable=self.UE4Path_text)
        UE4Path.grid(column=0, row=4, sticky='EW', padx=5, pady=5)
        UE4Btn = tk.Button(self,
                           text=u'Choose File',
                           command=self.OpenFileEditor)
        UE4Btn.grid(column=1, row=4, sticky='EW', padx=5, pady=5)

        text = paths_dict["UE4 Project"]
        self.UE4Project_text = tk.StringVar(self, value=text)
        ProjectPath = tk.Entry(self,
                               textvariable=self.UE4Project_text,)
        ProjectPath.grid(column=0, row=5, sticky='EW', padx=5, pady=5)
        ProjectBtn = tk.Button(self,
                               text=u'Choose File',
                               command=self.OpenFileProject)
        ProjectBtn.grid(column=1, row=5, sticky='EW', padx=5, pady=5)

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

    def OpenFileEditor(self):
        self.UE4Path_text.get()
        text = tkfile.askopenfilename()
        paths_dict["UE4 Editor"] = text
        self.UE4Path_text.set(text)
        path_json = os.path.abspath(
            "BatchLightUE4/Models/setup.json")
        with open(path_json, 'w') as f:
            json.dump(paths_dict, f, indent=4)

    def OpenFileProject(self):
        self.UE4Project_text.get()
        text = tkfile.askopenfilename()
        paths_dict["UE4 Project"] = text
        print("Text Field > ", text)
        print(paths_dict)
        path_json = os.path.abspath(
            "BatchLightUE4/Models/setup.json")
        self.UE4Project_text.set(text)
        with open(path_json, 'w') as f:
            json.dump(paths_dict, f, indent=4)

    def OnButtonClick(self):
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

        print('Index Level Rendering >> ', levels_rendering)
        self.labelVariable.set(text)
        if msg.askyesno('Launch Build', 'Lancement du calcul ?'):
            perforcecheckout(levels_rendering)
            buildmap(levels_rendering)