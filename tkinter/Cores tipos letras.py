from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")
menu_inicial.geometry("500x300")

label_1 = Label(menu_inicial,
                text="Este é o label 1",
                bg="#ffff00",
                fg="red",
                font="Arial")
label_1.pack()

label_2 = Label(menu_inicial,
                text="Este é o label 2",
                font="Arial 20 bold italic")

label_2.pack()

label_3 = Label(menu_inicial,
                text="Este é o label 3",
                font="Verdana 42 bold",
                fg="#aaaaaa")

label_3.pack()

# RGB #00FFff
# Red #
# Green
# Blue

menu_inicial.mainloop()
