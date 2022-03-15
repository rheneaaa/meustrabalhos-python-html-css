from tkinter import *

root = Tk()
root.geometry("300x200")

meuMenu = Menu(root)
def fileNew_click():
    print("fileNew_click")

# Menu File
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="New", command=fileNew_click)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
meuMenu.add_cascade(label="File", menu=fileMenu)

# Menu Edit
fileEdit = Menu(meuMenu, tearoff=0)
fileEdit.add_command(label="Copy")
fileEdit.add_command(label="Paste")
fileEdit.add_command(label="Select")
meuMenu.add_cascade(label="Edit", menu=fileEdit)

root.config(menu=meuMenu)

root.mainloop()

n = -1
while n != 0:#Menu interativo ainda em Desenvolvimento
    print(f""" 
      ### B-R-A Park ###
      1 - Consultar Vagas Livres
      2 - Cadastra Veiculo 
      3 - Buscar Veiculo por Placa
      4 - Ver Todas Vagas Ocupadas
      0 - Sair \n""")
    n = int(input('Escolha sua opção:'))
    print("\n")