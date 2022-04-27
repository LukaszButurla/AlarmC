from tkinter import Label
from Components.Style.style import gray
from datetime import datetime

class Clock:

    window = None

    def __init__(self, root):

        window = root
        self.ShowClock()


    def ShowClock(self):

        print("tak")

        txt_01 = Label(self.window, text = "10:10", anchor="nw", font=("", 20), bg = gray)
        txt_01.place(x = 276, y = 0)

    def Update(self):

        pass




