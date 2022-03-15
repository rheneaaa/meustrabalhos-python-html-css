from tkinter import *

root = Tk()

img = PhotoImage(file="images/imagem1.png")

label_imagem = Label(root, image=img).pack()


root.mainloop()
