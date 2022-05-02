from tkinter import Button
from tkinter.constants import BUTT
from Components.Timer.timer import Timer


class TimerBtn:

    frame = None
    timer = None
    btnStart = None
    btnStop = None
    btnReset = None
    start = False
    pause = False

    def __init__(self, frame):

        self.frame = frame
        self.timer = Timer(frame)
        self.AddButtons(frame)
        self.UpdateButtons()

    def AddButtons(self, frame):

        self.btnStart = Button(frame, text = "<", command = self.StartTimer)
        self.btnStop = Button(frame, text = "P", command = self.StopTimer)
        self.btnReset = Button(frame, text = "R", command = self.ResetTimer)


    def UpdateButtons(self):

        if self.start == False:

            self.btnStart.place(x = 180, y = 300, height=30, width=30)
            self.btnStop.place_forget()

        elif self.start == True:

            self.btnStart.place_forget()
            self.btnStop.place(x = 140, y = 300, height=30, width=30)

        if self.pause == True:

            self.btnReset.place(x = 100, y = 300, height=30, width=30)

        elif self.pause == False:

            self.btnReset.place_forget()




    def StartTimer(self):

        self.start = True
        self.UpdateButtons()
        self.timer.StartStop(self.start)
        print("start")


    def StopTimer(self):

        if self.pause == True:

            self.pause = False

        elif self.pause == False:

            self.pause = True

        self.UpdateButtons()

    def ResetTimer(self):

        self.start = False
        self.pause = False
        self.timer.ResetTime()
        self.UpdateButtons()