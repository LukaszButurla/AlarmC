from tkinter import *
from Components.Style.style import gray
from datetime import datetime
from time import time, sleep
from Components.Alarms.alarmManager import AlarmManager

class Clock:

    window = None
    hour = None
    minute = None

    def __init__(self, root):

        window = root       
        
        self.Load_time()
        self.ShowClock()

    def Load_time(self):

        self.hour = datetime.today().hour
        self.minute = datetime.today().minute

    def ShowClock(self):

        strHour = str(self.hour)
        strMinute = str(self.minute)

        if len(strMinute) == 1:
            self.minute = "0" + strMinute

        txt_01 = Label(self.window, text = "{}:{}".format(self.hour, self.minute), anchor="nw", font=("Calibri", 20), bg = gray)
        txt_01.place(x = 276, y = 0)


    def Update(self):

        while True:
            sleep(1 - time() % 1)

            print("2")


        




