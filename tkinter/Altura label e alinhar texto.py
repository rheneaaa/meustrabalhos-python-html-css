from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Rhene")
menu_inicial.geometry("500x500")

label1 = Label(menu_inicial,
               text="Frase de teste",
               font="Arial 20",
               bd=1,
               relief="solid",
               width=20,
               height=2,
               anchor=CENTER
).pack()


menu_inicial.mainloop()
