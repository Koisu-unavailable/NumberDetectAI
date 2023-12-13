import tkinter as tk
from windowManagment import drawingWindow, startUpWindow, window
class App():
    root = tk.Tk()
    mainFrame = tk.Frame(root)
    currentWindow : window.windowBase
    def __init__(self, root, mainFrame):
        self.root = root
        self.mainFrame = mainFrame
        print("App inited") 
    def run(self, root=root, mainFrame=mainFrame):
        self.currentWindow = startUpWindow.startUpWin(
            root,
            "Welcome to the number detection AI",
            body=mainFrame,
            rootApp=self,
            size="1080x720"
            )
        self.currentWindow.loadFrame()
        

if __name__ == "__main__":
    app = App()
    app.run()
    App.root.mainloop()