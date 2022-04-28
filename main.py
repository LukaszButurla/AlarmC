from time import sleep
from tkinter import *
from Components.Ui.ui import MainView
from Components.Clock.clock import Clock
from Components.Style.style import gray, width, height
from time import sleep, time


class Main:

    window = None
    clock = None
    ui = None

    def __init__(self):
        
        self.ConfigurateWindow()
        self.clock = Clock(self.window)  
        self.ui = MainView(self.window)
        self.Update()


    def ConfigurateWindow(self):
        
        self.window = Tk()

        self.window.geometry("{}x{}".format(width, height))
        self.window.configure(bg = gray)


    def test(self):

        self.window.configure(bg = "pink")

        
    def Update(self):

        while True:
                        
            sleep(0.1)          

            self.window.update()            
            self.clock.Load_time()
            self.clock.ShowClock()
        

if __name__ == "__main__":

    Main()



