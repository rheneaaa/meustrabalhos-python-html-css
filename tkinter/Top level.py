from tkinter import *

root = Tk()
root.geometry("300x200")


def abrir_formulario():
    # Top level
    top = Toplevel()
    top.title("Novo fromulario")
    top.geometry("200x100")
    lb1 = Label(top, text="Label na nova janela")
    lb1.pack()


btn = Button(root, text="Novo...", command=abrir_formulario)
btn.pack()


root.mainloop()
