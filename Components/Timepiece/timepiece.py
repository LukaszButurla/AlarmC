from tkinter import Label

class Timepiece:

    frame = None

    def __init__(self, frame):

        print("init timepiece")
        self.frame = frame
        self.ShowTimepiece()

    def ShowTimepiece(self):

        txt_timepiece = Label(self.frame, text = "Timepiece", anchor="nw")
        txt_timepiece.place(x = 10, y = 10, height=20, width=50)

