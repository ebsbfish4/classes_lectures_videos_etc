#! python3

from tkinter import *
from PIL import Image, ImageTK

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show Image', command = self.showImg)
        edit.add_command(label='Show Text', command = self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    # You can put this after refrenced in previous definition because python
    # does not run the function, call it, until something is run

    def client_exit(self):
        exit()

    def showImg(self):
        load = Image.open('pic.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text='Hey there')
        text.pack
        



root = Tk()
root.geometry("400x300")


app = Window(root)

root.mainloop()
