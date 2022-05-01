from tkinter import Frame, Label
from Components.Info.info import Info


class InfoPage:

    window = None
    frame = None
    info = None

    def __init__(self, root):

        self.window = root
        self.CreateInfoPage()
        self.info = Info(self.frame)

    def CreateInfoPage(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowInfoPage(self):

        self.frame.tkraise()

