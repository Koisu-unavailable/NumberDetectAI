import tkinter as tk

class buttonButWithId(tk.Button):
    buttonId : int
    def __init__(this, id, text, command, width, height):
        super().__init__(text=text, command=command, width=width, height=height)
        self.buttonId = id