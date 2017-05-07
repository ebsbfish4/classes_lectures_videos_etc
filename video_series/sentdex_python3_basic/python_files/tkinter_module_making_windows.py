#! python3

# tkinter is part of standard library. It is a wrapper around tk
# and tkl (?) that are eventually used to make windows

from tkinter import *

# we want to make our window class

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master



root = Tk()

app = Window(root)

root.mainloop()
