from tkinter.constants import BUTT
from Components.Timer import timer
from Components.Timer.timer import Timer
from tkinter import Button, Label, Frame


class TimerPage:

    window = None
    frame = None
    timer = None

    def __init__(self, root):

        print("init timer page")
        self.timer = Timer(self.frame)
        self.CreateTimerFrame()
        self.window = root


    def CreateTimerFrame(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "white")
        self.frame.place(x = 0, y = 0)



    def ShowTimerFrame(self):

        print("show timer frame")
        self.frame.tkraise()
        self.timer.ShowTimer()

