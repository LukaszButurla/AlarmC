from datetime import date, datetime
from tkinter import Label
from time import sleep, time, strftime
import time
from math import floor

class Timer:

    frame = None
    start = False
    timerV = 0
    timeStart = None
    txtTimer = None
    txtTime = "0:0:0"
    hour = 0
    minute = 0
    second = 0

    def __init__(self, frame):

        self.frame = frame
        print("init timer")
        self.ShowTimer()

    def ShowTimer(self):

        self.txtTimer = Label(self.frame, text = "0:00.00", font=("Calibri", 30), bg = "white", anchor="nw")
        self.txtTimer.place(x = 210, y = 180, anchor= "e")

    def EditTimer(self):

        self.txtTimer.configure(text = self.txtTime)

    def ResetTime(self):

        self.start = False
        self.timerV = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.txtTime = "{}:{}.{}".format(self.hour, self.minute, self.second)
        self.EditTimer()

    def StartStop(self, start):

        self.start = start


    def Count(self):

        if self.start == True:

            print(self.timerV)

            if self.timerV == 0:

                self.timeStart = time.time()
            
            self.timerV = time.time() - self.timeStart
            self.timerV = "{:.2f}".format(self.timerV)

            fTime = float(self.timerV)

            if fTime >= 3600:

                self.hour = fTime / 3600
                self.hour = floor(self.hour)
                fTime -= self.hour * 3600

            if fTime >= 60:

                self.minute = fTime / 60
                self.minute = floor(self.minute)
                fTime -= self.minute * 60

            if len(str(self.minute)) < 2:

                    self.minute = "0" + str(self.minute)


            self.second = fTime

            self.second = "{:.2f}".format(self.second)

            if len(str(self.second)) < 5:

                self.second = "0" + self.second


            self.txtTime = "{}:{}.{}".format(str(self.hour), self.minute, self.second)
            self.EditTimer()

            


    
            
            

