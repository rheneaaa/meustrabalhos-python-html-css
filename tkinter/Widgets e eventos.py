from tkinter import *

def mostrarNome():
    nome = textbox1.get()
    label2 = Label(root, text="O seu nome é " + nome)
    label2.grid()

root = Tk()
root.title("Título app")
root.geometry("200x100")


# Crias os widgets
label1 = Label(root, text="Escreve o seu nome:")
textbox1 = Entry(root)
button1 = Button(root, text="Executar", command=mostrarNome)


# Organizar widgets
label1.grid()
textbox1.grid()
button1.grid()


root.mainloop()
