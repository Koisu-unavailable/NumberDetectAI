import tkinter as tk
from windowManagment.window import *
from datasetCreation import createDataset
class drawingWindow(windowBase):
    name = "Placeholder"
    drawingResolution = "5x5"
    def loadFrame(self, drawingResolution=drawingResolution):
        #Create a grid of buttons
        for i in range(int(drawingResolution.split("x")[0])):
            for j in range(int(drawingResolution.split("x")[2])):
                tk.Button(command=createDataset.datasetCreator.numberToVector).grid(row=i, column=j)
    
