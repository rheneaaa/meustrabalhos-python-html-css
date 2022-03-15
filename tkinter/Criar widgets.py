from tkinter import *

# meu widgets
class FrameNome(Frame):
    def __init__(self, a):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        labelN = Label(self, text="Nome")
        textN = Entry(self)
        labelN.grid(row=0, column=0)
        textN.grid(row=0, column=1)


root = Tk()
root.title("App")

frameN1 = FrameNome(root).grid()
frameN2 = FrameNome(root).grid()
frameN3 = FrameNome(root).grid()
frameN4 = FrameNome(root).grid()


root.mainloop()
