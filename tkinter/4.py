from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Título")

label_1 = Label(menu_inicial, text="Este é o label 1.")
label_2 = Label(menu_inicial, text="Este é o label 2.")
cmd = Button(menu_inicial, text="Executar")

# pack
label_1.pack()
label_2.pack()
cmd.pack()


menu_inicial.mainloop()
