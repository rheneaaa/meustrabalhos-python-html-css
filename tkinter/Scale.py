from tkinter import *

root = Tk()
root.geometry("300x200")

def vervalor():
    print(slide.get())

slide = Scale(root, from_=0, to=100, orient=HORIZONTAL, resolution=5)
slide.pack()

cmd = Button(root, text="Ver valor", command=vervalor)
cmd.pack()

root.mainloop()
