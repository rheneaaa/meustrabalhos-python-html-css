from tkinter import *

class minhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self['height'] = 200
        self['width'] = 400
        self['bg'] = 'green'

root = Tk()

fmr1 = minhaFrame(root).pack()

root.mainloop()
