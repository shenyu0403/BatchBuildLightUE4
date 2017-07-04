import tkinter as tk

class SwarmUI(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent

    def initialize(self):
        self.grid()

        tk.Label(self, text="Test").grid()
