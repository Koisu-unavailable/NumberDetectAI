import tkinter as tk
from windowManagment.window import *
from windowManagment import drawingWindow
import main
class startUpWin(windowBase):
    rootApp : main.App
    body : tk.Frame 
    def __init__(self, root, name, body,rootApp, size):
        '''
        This window shows on startup
        '''
        super().__init__(root, name, size)
        self.body = body
        self.rootApp = rootApp
    def loadFrame(self):
        WelcomeText = tk.Label(self.body, text="Welcome to the number detection AI")
        WelcomeText.grid(row=0, column=1)
        openDrawWindowButton = tk.Button(
            self.body, text="Open drawing window", 
            command=lambda:self.switchWindow(drawingWindow.drawingWindow,self.rootApp),
            )
        openDrawWindowButton.grid(row=2, column=1)
        self.body.grid(row=0, column=0)
    def switchWindow(self, windowToSwitchTo : windowBase, App: main.App):
        self.clearFrame(self.body)
        App.currentWindow = windowToSwitchTo(self.root)
        App.currentWindow.loadFrame(App.mainFrame)
        
        
        
