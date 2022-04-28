from tkinter import *
from Components.Style.style import *
from functools import partial
from Components.Clock.clock import Clock
from Components.Alarms.alarmManager import AlarmManager

class MainView:

    def __init__(self, root):

        self.window = root

        self.ShowMenu()
        
    def ShowMenu(self):

        btnClock = Button(self.window, text = "C", command=partial(self.ShowMenu))
        btnClock.place(x = 180, y = 520)

        btnAlarm = Button(self.window, text = "A", command=partial(self.ShowMenu))
        btnAlarm.place(x = 200, y = 520)

        btnTimer = Button(self.window, text = "T", command=partial(self.ShowMenu))
        btnTimer.place(x = 220, y = 520)

        btnTime = Button(self.window, text = "P", command=partial(self.ShowMenu))
        btnTime.place(x = 160, y = 520)

        btnInfo = Button(self.window, text = "I", command=partial(self.ShowMenu))
        btnInfo.place(x = 240, y = 520)



        
    
