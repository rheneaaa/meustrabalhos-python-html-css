from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeiro app")
menu_inicial.geometry("500x300")
# menu_inicial["bg"] = "blue"

def cmd_Click(mensagem):
    print(mensagem)

# botão
cmd1 = Button(menu_inicial, text="Executar", command=lambda: cmd_Click("Nova mensagem"))
cmd1.pack()

cmd2 = Button(menu_inicial, text="Clicar", command=lambda: print('Ok'))
cmd2.pack()


# menu_inicial.geometry("500x250+700+350")
# menu_inicial.resizable(True, True)



# menu_inicial.minsize(500, 250)
# menu_inicial.maxsize(1200, 700)

# menu_inicial.state("iconic")

menu_inicial.mainloop()
