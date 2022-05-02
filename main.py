from time import sleep
from tkinter import *
from Components.Ui.ui import MainView
from Components.Clock.clock import Clock
from Components.Alarms.alarmManager import Alarms
from Components.Style.style import gray, width, height
from time import sleep, time 


class Main:

    window = None
    clock = None
    alarm = None
    ui = None
     
    def __init__(self):
        
        self.ConfigurateWindow()
        self.ui = MainView(self.window)
        self.Update()

         
    def ConfigurateWindow(self):
        

        self.window = Tk()

        self.window.geometry("{}x{}".format(width, height))
        self.window.configure(bg = "blue")
        
    def Update(self):

        while True:                           

            sleep(0.05)

            self.window.update()     
            self.ui.clockPage.clock.LoadTime()
            self.ui.clockPage.clock.ShowClock()  
            self.ui.timerPage.timerBtn.timer.Count()
        

if __name__ == "__main__":

    Main()


