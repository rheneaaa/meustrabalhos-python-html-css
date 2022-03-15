from tkinter import *
from tkinter import ttk
janela = Tk()
frm = ttk.Frame(janela, padding=10)
janela.geometry("200x100")
frm.grid()
ttk.Label(frm, text="Olá, Mundo!").grid(column=0, row=0)
ttk.Button(frm, text="Fechar", command=janela.destroy).grid(column=0, row=1)
janela.mainloop()
