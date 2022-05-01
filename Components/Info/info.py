from tkinter import Label

class Info:

    frame = None

    def __init__(self, frame):

        self.frame = frame
        self.ConfigureFrame()

    def ConfigureFrame(self):

        txt = Label(self.frame, text = "Info", anchor="nw", font=("Calibri", 20))
        txt.place(x = 10, y = 10)