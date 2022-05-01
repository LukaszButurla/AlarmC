from datetime import date, datetime
from tkinter import Label
from time import sleep, time
from tkinter.constants import SEL

class Timer:

    frame = None
    start = False
    timerV = 0
    t = 0

    def __init__(self, frame):

        self.frame = frame
        print("init timer")
        self.ShowTimer()

    def ShowTimer(self):

        txtTimer = Label(self.frame, text = self.timerV, anchor="nw", font=("Calibri", 20))
        txtTimer.place(x = 150, y = 150)

    
            
            

