from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Rhene")
menu_inicial.geometry("500x500")

texto = StringVar()
texto.set("Novo texto")

label1 = Label(menu_inicial,
               font="Arial 20",
               bg="red",
               fg="white",
               textvariable=texto)

texto.set("Rhene Alves")

label1.pack()

menu_inicial.mainloop()
