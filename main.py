from tkinter import *
from Components.Ui.ui import MainView
from Components.Clock.clock import Clock
from Components.Style.style import gray, width, height

class Main:

    window = None
    clock = None

    def __init__(self):

        self.ConfigurateWindow()
        clock = Clock(self.window)

        self.window.mainloop()

    window = None

    def ConfigurateWindow(self):

        self.window = Tk()

        self.window.geometry("{}x{}".format(width, height))
        self.window.configure(bg = gray)   

        


Main()



