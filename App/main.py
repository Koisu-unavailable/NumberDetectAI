import tkinter as tk
from windowManagment import drawingWindow as drawWin
class App():
    root = tk.Tk()
    def __init__(self) -> None:
        pass
    def run(self, root=root):
        currentWindow = drawWin.drawingWindow(root=root, name="AH")
        root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()