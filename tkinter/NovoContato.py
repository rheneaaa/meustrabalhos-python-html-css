from tkinter import *
import os

pastaApp = os.path.dirname(__file__)

def semComando():
    print("")

def novoContato():
    exec(open(pastaApp+"\\Testes finais 1.py").read())

app = Tk()
app.title("Senai")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Consultar Vagas", command=novoContato)
menuContatos.add_command(label="Cadastrar Veículos", command=novoContato)
menuContatos.add_command(label="Buscar Veículos (Placa)", command=semComando)
menuContatos.add_command(label="Vagas Ocupadas", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Menu", menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Senai", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)


app.mainloop()
