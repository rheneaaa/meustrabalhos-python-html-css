from tkinter import *

# Funções
def mostrarNome():
    vartexto.set(textbox1.get())

root = Tk()
root.title("Aplicação")

vartexto = StringVar()


# Widgets
label1 = Label(root, text="O seu nome é: ")
textbox1 = Entry(root)
button1 = Button(root, text="Executar", command=mostrarNome)
label2 = Label(root, textvariable=vartexto)

# Layout
label1.grid()
textbox1.grid()
button1.grid()
label2.grid()



root.mainloop()
