import tkinter as tk

class windowBase():
    '''
    This is the base for any tkinter window that I made
    '''
    name = ""
    windowSize = "1080x720"
    iconPath = ""
    body : tk.Frame
    def __init__(self, root, name=name, size=windowSize):
        '''
        Init initializes window metadata
        
        '''
        self.root : tk.Tk = root
        self.root.title(name)
        self.root.geometry(size)
    def clearFrame(self, body):
        for widgets in body.winfo_children():
            widgets.destroy()
    def loadFrame():
        '''
        Loads all widgets
        '''
        pass