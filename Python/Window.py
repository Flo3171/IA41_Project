from tkinter import *

class Window:

    def __init__(self, t):
        self.window = Tk()
        self.window.geometry(t)
        self.window.title("Rasend Robot")
        self.window.resizable(width=False, height=False)

    def launch(self):

        self.window.mainloop()