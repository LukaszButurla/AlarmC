from tkinter import Frame, Label
from Components.Timepiece import timepiece
from Components.Timepiece.timepiece import Timepiece

class TimepiecePage:

    window = None
    frame = None
    timepiece = None

    def __init__(self, root):

        print("init timepiece page")
        self.window = root
        self.CreateTimepiecePage()
        self.timepiece = Timepiece(self.frame)

    def CreateTimepiecePage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowTimepieceFrame(self):

        print("show timepiece page")
        self.frame.tkraise()