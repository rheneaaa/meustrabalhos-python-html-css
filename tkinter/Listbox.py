from tkinter import *

root = Tk()

lista = Listbox(root, selectmode=EXTENDED)
lista.pack()

# inserir um item de cada vez
#lista.insert(END, "Primeiro item da lista")
#lista.insert(END, "Segundo item da lista")
#lista.insert(END, "Terceiro item da lista")
#lista.insert(END, "Quarto item da lista")

# inserir vários itens de uma lista
nome = ['João', 'Ana', 'Carlos']
for i in nome:
    lista.insert(END, i)

def executar():
    print(lista.get(ACTIVE))

cmd = Button(root, text="Clique", command=executar).pack()

# lista.delete(1, 1)

root.mainloop()
