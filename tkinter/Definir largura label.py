from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")

label_1 = Label(menu_inicial,
                text="Este é o label 1",
                font="Arial 20",
                bg="red",
                width=20)

label_1.pack()

label_2 = Label(menu_inicial,
                text="Este é o label 2",
                font="Arial 40",
                bg="red",
                width=20)
label_2.pack()

menu_inicial.mainloop()
