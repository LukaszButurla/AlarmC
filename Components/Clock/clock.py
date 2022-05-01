from tkinter import *
from Components.Style.style import gray
from datetime import datetime
from time import time, sleep

class Clock:

    window = None
    hour = None
    minute = None
    frame = None

    def __init__(self, frame):   

        self.frame = frame
        print("frame:", frame)
        print("self frame:", self.frame)
        print("init clock")

    def LoadTime(self):

        self.hour = datetime.today().hour
        self.minute = datetime.today().minute

    def ShowClock(self):

        strMinute = str(self.minute)

        if len(strMinute) == 1:
            self.minute = "0" + strMinute

        txt_01 = Label(self.frame, text = "{}:{}".format(self.hour, self.minute), anchor="nw", font=("Calibri", 20), bg = "white")
        txt_01.place(x = 140, y = 350)

    def Update(self):
          
        self.LoadTime()
        self.ShowClock()
    


        




