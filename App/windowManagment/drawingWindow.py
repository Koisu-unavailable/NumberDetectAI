import tkinter as tk
from windowManagment.window import *
from datasetCreation import createDataset
class drawingWindow(windowBase):
    name = "Placeholder"
    drawingResolution = "5x5"
    
    def loadFrame(self,body, drawingResolution=drawingResolution ):
        self.body = body
        for i in range(int(drawingResolution.split("x")[0])):
            for j in range(int(drawingResolution.split("x")[1])):
                tk.Button(self.body, command=createDataset.datasetCreator.numberToVector, width=10,height=10).grid(row=i, column=j)
    
