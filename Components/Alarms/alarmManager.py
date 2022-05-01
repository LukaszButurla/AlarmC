from tkinter import Label

class Alarms:

    frame = None

    def __init__(self, frame):

        self.frame = frame
        self.ShowAlarms()

    def ShowAlarms(self):

        txt_a = Label(self.frame, text = "Alarms", anchor="nw", font=("Calibri", 20))
        txt_a.place(x = 100, y = 100)