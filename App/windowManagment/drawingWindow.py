import tkinter as tk
from windowManagment.window import *
from datasetCreation import createDataset
import random as rdm
from CustomTkElements import buttonButWithId
class drawingWindow(windowBase):
    name = "Placeholder"
    drawingResolution = "6x6"
    def loadFrame(self,body, drawingResolution=drawingResolution ):
        self.body = body
        self.drawNumText = tk.Label(master=self.body,text=rdm.randint(1,10)).grid(row=0, column=2)
        for i in range(int(drawingResolution.split("x")[0])):
            for j in range(int(drawingResolution.split("x")[1])):
                self.currButton = buttonButWithId.buttonButWithId(
                self.body, 
                command=lambda: self.buttonClicked(self.currButton),
                width=5,
                height=5,
                id=i
                )
                self.currButton.grid(row=i+2, column=j+2)
    def buttonClicked(self, button):
        if "self.numArray" not in locals():
            print("Doesn't exist")
            self.numArray = [0] * 25
        else:
            print(self.numArray)
            self.numArray[button.id] = 1