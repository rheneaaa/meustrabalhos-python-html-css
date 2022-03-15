from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Rhene")
menu_inicial.geometry("500x500")

label1 = Label(
    menu_inicial,
    text="Frase de teste\nOutro texto",
    font="Arial 20",
    bd=1,
    relief="solid",
    padx=50, # espaço começo e fim da frase
    pady=50, # espaço acima e abaixo da frase
    justify=RIGHT # justifica texto

).pack()



menu_inicial.mainloop()
