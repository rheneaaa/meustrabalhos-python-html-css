from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x500")

border = 6

label1 = Label(menu_inicial,
    text="solid",
    font="Arial 20",
    bd=border,
    relief="solid")

label1.pack()

label1 = Label(menu_inicial,
    text="flat",
    font="Arial 20",
    bd=border,
    relief="flat")

label1.pack()

label1 = Label(menu_inicial,
    text="sunken",
    font="Arial 20",
    bd=border,
    relief="sunken")

label1.pack()

label1 = Label(menu_inicial,
    text="ridge",
    font="Arial 20",
    bd=border,
    relief="ridge")

label1.pack()

label1 = Label(menu_inicial,
    text="groove",
    font="Arial 20",
    bd=border,
    relief="groove")

label1.pack()

label1 = Label(menu_inicial,
    text="raised",
    font="Arial 20",
    bd=border,
    relief="raised")

label1.pack()

menu_inicial.mainloop()
