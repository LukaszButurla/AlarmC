from Components.Alarms.alarmManager import Alarms
from tkinter import Frame

class AlarmsPage:

    alarms = None
    window = None
    frame = None

    def __init__(self, root):

        print("Alarm page Init")
        self.window = root
        self.CreateAlarmsPage()
        self.alarms = Alarms(self.frame)

    def CreateAlarmsPage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowAlarmsPage(self):

        self.frame.tkraise()


