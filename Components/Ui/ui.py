from tkinter.constants import N
from Components.Style.style import *
from Components.Clock.clock import Clock
from Components.Alarms.alarmManager import Alarms
from functools import partial
from tkinter import PhotoImage, Button
from Pages.alarmsPage import AlarmsPage
from Pages.clockPage import ClockPage
from Pages.timerPage import TimerPage
from Pages.infoPage import InfoPage
from Pages.timepiecePage import TimepiecePage

class MainView:

    window = None
    timerPage = None
    clockPage = None
    alarmsPage = None
    infoPage = None
    timepiecePage = None

    def __init__(self, root):

        print("UI Init")

        self.window = root 
        self.timerPage = TimerPage(self.window)
        self.alarmsPage = AlarmsPage(self.window)
        self.infoPage = InfoPage(self.window)
        self.timepiecePage = TimepiecePage(self.window)
        self.clockPage = ClockPage(self.window)
        self.ShowMenu()

        
    def ShowMenu(self):
        
        btnClock = Button(self.window, command=partial(self.MenuClock))
        btnClock.place(x = 0, y = 490, height=60, width=60)

        btnAlarm = Button(self.window, command=partial(self.MenuAlarm))
        btnAlarm.place(x = 60, y = 490, height=60, width=60)

        btnTimer = Button(self.window, command=partial(self.MenuTimepiece))
        btnTimer.place(x = 120, y = 490, height=60, width=60)

        btnTime = Button(self.window, command=partial(self.MenuTimer))
        btnTime.place(x = 180, y = 490, height=60, width=60)

        btnInfo = Button(self.window, command=partial(self.MenuInfo))
        btnInfo.place(x = 240, y = 490, height=60, width=60)

    def MenuClock(self):

        print("clock btn")        
        self.clockPage.ShowClockFrame()
        

    def MenuAlarm(self):
        
        print("alarm btn")
        self.alarmsPage.ShowAlarmsPage()
        

    def MenuTimepiece(self):

        print("timepiece btn")
        self.timepiecePage.ShowTimepieceFrame()

    def MenuTimer(self):

        print("timer btn")
        self.timerPage.ShowTimerFrame()

    def MenuInfo(self):

        print("Info btn")
        self.infoPage.ShowInfoPage()



        
    
