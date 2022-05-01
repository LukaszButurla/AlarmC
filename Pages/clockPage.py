from Components.Clock import clock
from Components.Clock.clock import Clock
from tkinter import Label, Frame


class ClockPage:

    window = None
    clock = None
    frame = None

    def __init__(self, root):

        print("Init clock page")
        self.window = root
        self.CreateClockPage()
        self.clock = Clock(self.frame)


    def CreateClockPage(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowClockFrame(self):

        print("show clock frame")
        self.frame.tkraise()
        self.clock.Update()