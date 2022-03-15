from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeiro app")

menu_inicial.geometry("500x250+700+350")
menu_inicial.resizable(True, True)
menu_inicial.iconbitmap("images/icon.ico")


# menu_inicial.minsize(500, 250)
# menu_inicial.maxsize(1200, 700)

# menu_inicial.state("iconic")

menu_inicial.mainloop()